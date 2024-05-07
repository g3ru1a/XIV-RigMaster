bl_info = {
    "name": "XIV Bone Cleaner",
    "id_name": "xivbc",
    "author": "G3ru1a",
    "version": (0, 1),
    "blender": (4, 0, 0),
    "location": "View3D > UI > XIV Bone Cleaner",
    "description": "Cleans up the bones from a Meddle Exported .gltf Model",
    "warning": "",
    "doc_url": "",
    "category": "XIV Bone Cleaner 0.1",
}

import bpy, mathutils, math

class XIVBCMainPanel(bpy.types.Panel):
    bl_label = bl_info['name']
    bl_idname = bl_info['id_name']
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = bl_info['category']
    
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
#        row.operator("xivbc.show_clothes")
        row.operator("xivbc.toggle_hands")
        
    
class ToggleHandBones(bpy.types.Operator):
    bl_label = "Toggle Hands"
    bl_idname = "xivbc.toggle_hands"
    
    def execute(self, context):
        # Check if an Armature is selected
        # Get the armature object
        armature = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        
        # toggle_bone_visibility_array(armature, hand_bones_left)
        # toggle_bone_visibility_array(armature, hand_bones_right)
        
        return {'FINISHED'}

    
