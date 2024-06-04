
from ..utils.config import config
import bpy, mathutils, math

class VIEW3D_PT_LegacyPanel(bpy.types.Panel):
    bl_label = "Endwalker Armatures"
    bl_idname = "VIEW3D_PT_LegacyPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = config.category
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        # row.label(text = "Test")
        # row.operator("xivbc.test")
        row = layout.row()
        row.label(text = "Step 1.")
        row.operator("xivbc.armature_fixer")
        
        row = layout.row()
        row.label(text = "Step 2.")
        row.operator("xivbc.bone_cleanup")
        
        row = layout.row()
        row.label(text = "Step 3. Get to work!")
        row = layout.row()
        row.label(text="Toggle Bone Visibility")

        row = layout.row()
        row.operator("xivbc.toggle_clothes")
        row.operator("xivbc.toggle_gear")

        row = layout.row()
        row.operator("xivbc.toggle_face")
        row.operator("xivbc.toggle_hair")

        row = layout.row()
        row.operator("xivbc.toggle_twist")
        row.operator("xivbc.toggle_tail")
    
