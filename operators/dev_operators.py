import bpy, io, os, yaml # type: ignore
import string, random, pathlib
from ..utils.config import data as config
from ..utils.tools import mode_set, get_addon_absolute_path, import_shape_collection, lists_are_equal
from ..utils.armature import RM_Armature

class MyDumper(yaml.SafeDumper):
    pass

def represent_list(dumper, data):
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)

MyDumper.add_representer(list, represent_list)

class WM_OT_ShowMessage(bpy.types.Operator):
    bl_idname = "wm.show_message"
    bl_label = "Action Executed"

    message: bpy.props.StringProperty(name="Message", default="Action completed successfully!") # type: ignore

    def execute(self, context):
        self.report({'INFO'}, self.message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.label(text=self.message)

class ARMATURE_OT_ExportBonesToYAML(bpy.types.Operator):
    """Export current armature shapes to YAML File"""
    bl_label = "Export To YAML"
    bl_idname = ".".join((config["id_name"], "export_to_yaml"))
    
    def execute(self, context):
         # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            self.report({"ERROR"},"The active object is not an armature.")
            return {'CANCELLED'}
        
        # Loop through all the bones and write changes of only bones that have a custom shape attached
        data = {};
        with mode_set(mode="POSE"):
            for bone in armature.pose.bones:
                if bone.custom_shape:
                    data[str(bone.name)] = {
                            "name": str(bone.name),
                            "visible": not bone.bone.hide,
                            "shape": bone.custom_shape.name if bone.custom_shape else "None",
                            "color": bone.color.palette,
                            "transforms": {
                                "default": {
                                    "scale": list(bone.custom_shape_scale_xyz),
                                    "offset": list(bone.custom_shape_translation),
                                    "rotation": list(bone.custom_shape_rotation_euler)
                                }
                            }
                        }
        
        # Compute absolute path
        filename = context.scene.dev_props.dump_file_name
        filename = ".".join((filename, "yaml"))
        dump_file_path = os.path.join(get_addon_absolute_path(), config["yaml_files_folder"], filename)

        # Delete the file if it exists
        my_file = pathlib.Path(dump_file_path)
        if my_file.is_file():
            my_file.unlink()

        # Write new file 
        with io.open(dump_file_path, 'x') as outfile:
            yaml.dump(data, outfile, Dumper=MyDumper, default_flow_style=False, allow_unicode=True)
        
        # Show confirmation Popup
        bpy.ops.wm.show_message('INVOKE_DEFAULT', message="YAML File generated successfully!")
        return {'FINISHED'}
    
class ARMATURE_OT_ApplyYAMLCustomShapes(bpy.types.Operator):
    """Apply sesttings from YAML File"""
    bl_label = "Apply from YAML"
    bl_idname = ".".join((config["id_name"], "apply_from_yaml"))

    def execute(self, context):
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            self.report({"ERROR"},"The active object is not an armature.")
            return {'CANCELLED'}
        # Import blend file with custom shapes
        shapes = import_shape_collection(config["custom_shapes_filename"])
        
        # Get absolute path of yaml file
        filename = context.scene.dev_props.preview_yaml_files
        # filename = ".".join((filename, "yaml"))
        file_path = os.path.join(get_addon_absolute_path(), config["yaml_files_folder"], filename)

        # Get Variant key
        variant = context.scene.dev_props.preview_variants

        # Mak sure the file exists
        my_file = pathlib.Path(file_path)
        if not my_file.is_file():
            bpy.ops.wm.show_message('INVOKE_DEFAULT', message="Could not find YAML file.")
            return {'CANCELLED'}

        # Load the file data
        with io.open(file_path, 'r') as stream:
            data = yaml.safe_load(stream)

        # Apply changes
        rma = RM_Armature(armature=armature)
        for obj in data:
            values = data[obj]
            
            transforms = values["transforms"]["default"]
            if variant in values["transforms"].keys():
                transforms.update(values["transforms"][variant])

            scale = transforms["scale"]
            offset = transforms["offset"]
            rotation = transforms["rotation"]
            # transforms = values["transforms"][variant]
            # if transforms is None:
            #     transforms = values["transforms"]["default"]
            bone = rma.get_bone(obj)
            bone.set_custom_shape(shapes.get(values["shape"]), scale=scale)
            bone.set_custom_shape_offset(offset)
            bone.set_custom_shape_rotation_euler(rotation)
            bone.set_custom_shape_color(values["color"])
        
        # Show confirmation Popup
        bpy.ops.wm.show_message('INVOKE_DEFAULT', message="Custom Shapes Applied!")
        return {'FINISHED'}
    
class ARMATURE_OT_AppendVariantToYAML(bpy.types.Operator):
    """Append current differences as Variant to YAML File"""
    bl_label = "Export To YAML"
    bl_idname = ".".join((config["id_name"], "append_variant_to_yaml"))
    
    def execute(self, context):
         # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            self.report({"ERROR"},"The active object is not an armature.")
            return {'CANCELLED'}
        
        # Compute absolute path for the YAML file
        filename = context.scene.dev_props.yaml_files
        # filename = ".".join((filename, "yaml"))
        dump_file_path = os.path.join(get_addon_absolute_path(), config["yaml_files_folder"], filename)

        # Makse sure the file exists
        my_file = pathlib.Path(dump_file_path)
        if not my_file.is_file():
            bpy.ops.wm.show_message('INVOKE_DEFAULT', message="Could not find YAML file.")
            return {'CANCELLED'}

        # Load the file data
        with io.open(dump_file_path, 'r') as stream:
            data = yaml.safe_load(stream)

        # Get Variant key
        variant = context.scene.dev_props.variants

        # Go through each bone check if it has a custom shape, and if it's already in the YAML file compare
        # values. If the values are the same, move on. If the values differ add them as a variant
        with mode_set(mode="POSE"):
            for bone in armature.pose.bones:
                if bone.custom_shape:
                    scale_list = list(bone.custom_shape_scale_xyz)
                    offset_list = list(bone.custom_shape_translation)
                    rotation_list = list(bone.custom_shape_rotation_euler)
                    diff = {}
                    saved_transforms = data[str(bone.name)]["transforms"]["default"]
                    # Check scale
                    if not lists_are_equal(saved_transforms["scale"], scale_list):
                        diff["scale"] = scale_list
                    # Check offset
                    if not lists_are_equal(saved_transforms["offset"], offset_list):
                        diff["offset"] = offset_list
                    # Check rotation
                    if not lists_are_equal(saved_transforms["rotation"], rotation_list):
                        diff["rotation"] = rotation_list

                    # Check if diff is not empty
                    if diff:
                        data[str(bone.name)]["transforms"][variant] = diff
        
        # Delete YAML file
        my_file.unlink()

        # Write new data
        with io.open(dump_file_path, 'x') as outfile:
            yaml.dump(data, outfile, Dumper=MyDumper, default_flow_style=False, allow_unicode=True)
        bpy.ops.wm.show_message('INVOKE_DEFAULT', message="Updated YAML File!")
        return {'FINISHED'}

