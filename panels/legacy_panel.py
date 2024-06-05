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
        row.operator(".".join((config.id_name, "pose_reset_legacy")))
        
        row = layout.row()
        row.label(text = "Step 2.")
        row.operator(".".join((config.id_name, "custom_shapes_legacy")))
        
        row = layout.row()
        row.label(text = "Step 3. Get to work!")
        row = layout.row()
        row.label(text="Toggle Bone Visibility")

        row = layout.row()
        row.operator(".".join((config.id_name, "toggle_clothes_legacy")))
        row.operator(".".join((config.id_name, "toggle_gear_legacy")))

        row = layout.row()
        row.operator(".".join((config.id_name, "toggle_face_legacy")))
        row.operator(".".join((config.id_name, "toggle_hair_legacy")))

        row = layout.row()
        row.operator(".".join((config.id_name, "toggle_twist_legacy")))
        row.operator(".".join((config.id_name, "toggle_tail_legacy")))
    
