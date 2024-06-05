from ..utils.config import data as config
from ..utils import yaml_files
import bpy

def yaml_files_enum_callback(self, context):
    return yaml_files.get_master_files()

def variants_enum_callback(self, context):
    return config["variants"]

class StepsProperties(bpy.types.PropertyGroup):
    variants: bpy.props.EnumProperty(
        name="Variants Enum",
        description="Choose A Variant",
        items=variants_enum_callback
    ) # type: ignore
    yaml_files: bpy.props.EnumProperty(
        name="No YAML files found.",
        description="Choose A YAML File",
        items=yaml_files_enum_callback
    ) # type: ignore

class VIEW3D_PT_StepsPanel(bpy.types.Panel):
    bl_label = "Dawntrail Armatures Setup"
    bl_idname = "VIEW3D_PT_StepsPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = config["category"]
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.steps_props

        row = layout.row()
        layout.prop(props, "yaml_files", text="YAML")

        row = layout.row()
        layout.prop(props, "variants", text="Variant")
        row = layout.row()
        row.operator(".".join((config["id_name"], "custom_shapes")))
    
