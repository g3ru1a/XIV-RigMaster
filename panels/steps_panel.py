from ..utils.config import config
import bpy, mathutils, math

class VIEW3D_PT_StepsPanel(bpy.types.Panel):
    bl_label = "Dawntrail Armatures Setup"
    bl_idname = "VIEW3D_PT_StepsPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = config.category
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator(".".join((config.id_name, "custom_shapes")))
    
