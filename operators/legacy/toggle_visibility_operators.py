import bpy
from ...utils import LegacyBoner
from ...utils import bones;
from ...utils.config import config

class ARMATURE_OT_ToggleClothes(bpy.types.Operator):
    bl_label = "Clothes"
    bl_idname = ".".join((config.id_name, "toggle_clothes"))
    
    def execute(self, context):
        
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        
        # Cloth Bones
        for bone_name in bones.cloth_back_left:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        for bone_name in bones.cloth_front_left:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        for bone_name in bones.cloth_side_left:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()
        
        for bone_name in bones.cloth_back_right:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        for bone_name in bones.cloth_front_right:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        for bone_name in bones.cloth_side_right:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()


        return {'FINISHED'}
    
class ARMATURE_OT_ToggleGear(bpy.types.Operator):
    bl_label = "Gear"
    bl_idname = ".".join((config.id_name, "toggle_gear"))
    
    def execute(self, context):
        
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        
        bone_list = [bones.elbow_gear_left, bones.shoulder_gear_left, bones.elbow_gear_right, bones.shoulder_gear_right,
                     bones.waist_gear_left, bones.waist_gear2_left, bones.waist_gear_right, bones.waist_gear2_right,
                     bones.knee_gear_left, bones.knee_gear_right, bones.shield_left, bones.shield_right, 
                     bones.back_gear_left, bones.back_gear_right]

        for bone_name in bone_list:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        return {'FINISHED'}
    
class ARMATURE_OT_ToggleFace(bpy.types.Operator):
    bl_label = "Face"
    bl_idname = ".".join((config.id_name, "toggle_face"))
    
    def execute(self, context):
        
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        
        bone_list = [bones.jaw, bones.mouth_bottom, bones.mouth_upper, bones.corner_lip_left, bones.corner_lip_right,
                     bones.lip_bottom, bones.lip_upper, bones.cheek_left, bones.cheek_right, bones.nose,
                     bones.eyelid_left_bottom, bones.eyelid_left_top, bones.eyelid_right_bottom, 
                     bones.eyelid_right_top, bones.eyebrow_left_inner, bones.eyebrow_left_main,
                     bones.eyebrow_right_inner, bones.eyebrow_right_main, bones.ear_left, bones.ear_right,
                     bones.eye_left, bones.eye_right, bones.eye_corner_inner]
        for bone_name in bone_list:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        return {'FINISHED'}
    
class ARMATURE_OT_ToggleHair(bpy.types.Operator):
    bl_label = "Hair"
    bl_idname = ".".join((config.id_name, "toggle_hair"))
    
    def execute(self, context):
        
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        
        bone_list = [bones.hair_left, bones.hair_back, bones.hair_right, bones.hair_front, bones.hair_extensions_left,
                     bones.hair_extensions_right]
        bone_list += bones.hair_long
        bone_list += bones.earring_left
        bone_list += bones.earring_right
        for bone_name in bone_list:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        return {'FINISHED'}
        
class ARMATURE_OT_ToggleTwist(bpy.types.Operator):
    bl_label = "Twist"
    bl_idname = ".".join((config.id_name, "toggle_twist"))
    
    def execute(self, context):
        
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        
        bone_list = [bones.forearm_twist_left, bones.forearm_twist_right, bones.shoulder_twist_left,
                     bones.shoulder_twist_right, bones.upperarm_twist_left, bones.upperarm_twist_right]
        for bone_name in bone_list:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        return {'FINISHED'}
        
class ARMATURE_OT_ToggleTail(bpy.types.Operator):
    bl_label = "Tail"
    bl_idname = ".".join((config.id_name, "toggle_tail"))
    
    def execute(self, context):
        
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        
        bone_list = bones.tail
        for bone_name in bone_list:
            LegacyBoner.PoseBone(armature, bone_name).toggleVisibility()

        return {'FINISHED'}