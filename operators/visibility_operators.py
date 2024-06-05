import bpy
from ..utils.config import config
from ..utils.armature import RM_Armature
from ..utils.sections.extras import Clothing, Gear
from ..utils.sections.upper_body import LeftHand, RightHand, Hands, LeftArm, RightArm, Arms, TwistBones
from ..utils.sections.lower_body import Legs, LeftLeg, RightLeg, Waist, Tail

class ARMATURE_OT_BaseToggleVisibility(bpy.types.Operator):
    """Base class for toggling visibility of armature components"""
    bl_label = "Base Toggle Visibility"
    bl_idname = ".".join((config.id_name, "base_toggle_visibility"))
    armature_type = None
    visibility_props = None
    
    def execute(self, context):
         # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            self.report({"ERROR"},"The active object is not an armature.")
            return {'CANCELLED'}
        # shapes = import_shape_collection(config.custom_shapes_filename)
        rm_armature = RM_Armature(armature=armature)
        if self.armature_type is not None:
            visible: bool = self.armature_type(armature=rm_armature).toggle_visibility()
        for prop in self.visibility_props:
            setattr(context.scene.visibility_props, prop, visible)
        return {'FINISHED'}

class ARMATURE_OT_ToggleClothing(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Clothing"
    bl_idname = ".".join((config.id_name, "toggle_clothing"))
    armature_type = Clothing
    visibility_props = ["clothing_visible"]
    
class ARMATURE_OT_ToggleGear(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Gear"
    bl_idname = ".".join((config.id_name, "toggle_gear"))
    armature_type = Gear
    visibility_props = ["gear_visible"]
    
class ARMATURE_OT_ToggleHands(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Hands"
    bl_idname = ".".join((config.id_name, "toggle_hands"))
    armature_type = Hands
    visibility_props = ["left_hand_visible", "right_hand_visible"]

class ARMATURE_OT_ToggleArms(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Arms"
    bl_idname = ".".join((config.id_name, "toggle_arms"))
    armature_type = Arms
    visibility_props = ["left_arm_visible", "right_arm_visible"]

class ARMATURE_OT_ToggleLegs(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Legs"
    bl_idname = ".".join((config.id_name, "toggle_legs"))
    armature_type = Legs
    visibility_props = ["left_leg_visible", "right_leg_visible"]

class ARMATURE_OT_ToggleTwist(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Twists"
    bl_idname = ".".join((config.id_name, "toggle_twists"))
    armature_type = TwistBones
    visibility_props = ["twists_visible"]

class ARMATURE_OT_ToggleTail(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Tail"
    bl_idname = ".".join((config.id_name, "toggle_tail"))
    armature_type = Tail
    visibility_props = ["tail_visible"]

class ARMATURE_OT_ToggleLeftHand(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Left Hand"
    bl_idname = ".".join((config.id_name, "toggle_left_hand"))
    armature_type = LeftHand
    visibility_props = ["left_hand_visible"]

class ARMATURE_OT_ToggleRightHand(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Right Hand"
    bl_idname = ".".join((config.id_name, "toggle_right_hand"))
    armature_type = RightHand
    visibility_props = ["right_hand_visible"]

class ARMATURE_OT_ToggleLeftArm(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Left Arm"
    bl_idname = ".".join((config.id_name, "toggle_left_arm"))
    armature_type = LeftArm
    visibility_props = ["left_arm_visible"]

class ARMATURE_OT_ToggleRightArm(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Right Arm"
    bl_idname = ".".join((config.id_name, "toggle_right_arm"))
    armature_type = RightArm
    visibility_props = ["right_arm_visible"]

class ARMATURE_OT_ToggleLeftLeg(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Left Leg"
    bl_idname = ".".join((config.id_name, "toggle_left_leg"))
    armature_type = LeftLeg
    visibility_props = ["left_leg_visible"]

class ARMATURE_OT_ToggleRightLeg(ARMATURE_OT_BaseToggleVisibility):
    bl_label = "Right Leg"
    bl_idname = ".".join((config.id_name, "toggle_right_leg"))
    armature_type = RightLeg
    visibility_props = ["right_leg_visible"]

