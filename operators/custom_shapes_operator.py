import bpy, io, os, yaml # type: ignore
import pathlib
from ..utils.config import data as config
from ..utils.tools import get_addon_absolute_path, import_shape_collection
from ..utils.armature import RM_Armature


class ARMATURE_OT_CustomShapes(bpy.types.Operator):
    bl_label = "Apply Custom Shapes"
    bl_idname = ".".join((config["id_name"], "custom_shapes"))

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
        filename = context.scene.steps_props.yaml_files
        # filename = ".".join((filename, "yaml"))
        file_path = os.path.join(get_addon_absolute_path(), config["rig_master_files"], filename)

        # Get Variant key
        variant = context.scene.steps_props.variants

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
            
            # If there's a variant transform merge with the 
            # default to add missing keys (rotation, scale, offset) if there are any
            transforms = values["transforms"]["default"]
            if variant in values["transforms"].keys():
                transforms.update(values["transforms"][variant])

            scale = transforms["scale"]
            offset = transforms["offset"]
            rotation = transforms["rotation"]

            # Edit Bone
            bone = rma.get_bone(obj)
            bone.set_custom_shape(shapes.get(values["shape"]), scale=scale)
            bone.set_custom_shape_offset(offset)
            bone.set_custom_shape_rotation_euler(rotation)
            bone.set_custom_shape_color(values["color"])
        
        # Show confirmation Popup
        bpy.ops.wm.show_message('INVOKE_DEFAULT', message="Custom Shapes Applied!")
        return {'FINISHED'}