import bpy
from ..utils.config import config

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
        row.operator(".".join((config.id_name, "pose_reset")))
        
        row = layout.row()
        row.label(text = "Step 2.")
        row.operator(".".join((config.id_name, "custom_shapes")))
        
        row = layout.row()
        row.label(text = "Step 3. Get to work!")
        row = layout.row()
        row.label(text="Toggle Bone Visibility")

        row = layout.row()
        row.operator(".".join((config.id_name, "toggle_clothes")))
        row.operator(".".join((config.id_name, "toggle_gear")))

        row = layout.row()
        row.operator(".".join((config.id_name, "toggle_face")))
        row.operator(".".join((config.id_name, "toggle_hair")))

        row = layout.row()
        row.operator(".".join((config.id_name, "toggle_twist")))
        row.operator(".".join((config.id_name, "toggle_tail")))
    
