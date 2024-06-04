import bpy, mathutils, math, os
from ...utils import LegacyBoner
from ...utils.config import config
from ...utils import bones;

class ARMATURE_OT_CustomShapes(bpy.types.Operator):
    bl_label = "Apply Custom Shapes"
    bl_idname = ".".join((config.id_name, "custom_shapes"))
    
    def execute(self, context):
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        # Check if the collection already exists
        shapes = self.importShapeCollection()
        
        #Setup Bones
        # Root Bones
        LegacyBoner.PoseBone(armature, "n_hara").custom_shape(shapes.get("Circle"), color="THEME12", scale=(0.04,1,0.04))
        LegacyBoner.PoseBone(armature, "n_root").custom_shape(shapes.get("Circle"), color="THEME12", scale=(0.2,1,0.2))
        
        # Hand Bones
        hand_bones_scale = (0.2,1,0.2)
        hand_bones_color = "THEME09"
        hand_bones_shape = shapes.get("Circle")
        for bone_name in bones.fingers_left:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(hand_bones_shape, color=hand_bones_color, scale=hand_bones_scale)
        for bone_name in bones.fingers_right:
             LegacyBoner.PoseBone(armature, bone_name).custom_shape(hand_bones_shape, color=hand_bones_color, scale=hand_bones_scale)
        
        # Arm Twist Bones
        LegacyBoner.PoseBone(armature, bones.forearm_twist_left).custom_shape(shapes.get("Sphere"), color="THEME05", scale=(.2,.2,.2))
        LegacyBoner.PoseBone(armature, bones.upperarm_twist_left).custom_shape(shapes.get("Sphere"), color="THEME05", scale=(.3,.3,.3))
        LegacyBoner.PoseBone(armature, bones.shoulder_twist_left).custom_shape(shapes.get("Sphere"), color="THEME05", scale=(.1,.1,.1))
        LegacyBoner.PoseBone(armature, bones.forearm_twist_right).custom_shape(shapes.get("Sphere"), color="THEME05", scale=(.2,.2,.2))
        LegacyBoner.PoseBone(armature, bones.upperarm_twist_right).custom_shape(shapes.get("Sphere"), color="THEME05", scale=(.3,.3,.3))
        LegacyBoner.PoseBone(armature, bones.shoulder_twist_right).custom_shape(shapes.get("Sphere"), color="THEME05", scale=(.1,.1,.1))

        # Gear Bones
        LegacyBoner.PoseBone(armature, bones.elbow_gear_left).custom_shape(shapes.get("Cube"), color="THEME08", scale=(.2,.2,.2))
        LegacyBoner.PoseBone(armature, bones.shoulder_gear_left).custom_shape(shapes.get("Cube"), color="THEME08", scale=(.1,.1,.1))
        LegacyBoner.PoseBone(armature, bones.elbow_gear_right).custom_shape(shapes.get("Cube"), color="THEME08", scale=(.2,.2,.2))
        LegacyBoner.PoseBone(armature, bones.shoulder_gear_right).custom_shape(shapes.get("Cube"), color="THEME08", scale=(.1,.1,.1))
        
        LegacyBoner.PoseBone(armature, bones.waist_gear_left).custom_shape(shapes.get("Arrow"), color="THEME08", scale=(1,1,1), rotation=(math.radians(-90), 0, 0))
        LegacyBoner.PoseBone(armature, bones.waist_gear2_left).custom_shape(shapes.get("Arrow"), color="THEME08", scale=(1,1,1), rotation=(math.radians(-90), 0, 0))
        LegacyBoner.PoseBone(armature, bones.waist_gear_right).custom_shape(shapes.get("Arrow"), color="THEME08", scale=(1,1,1), rotation=(math.radians(-90), 0, 0))
        LegacyBoner.PoseBone(armature, bones.waist_gear2_right).custom_shape(shapes.get("Arrow"), color="THEME08", scale=(1,1,1), rotation=(math.radians(-90), 0, 0))

        LegacyBoner.PoseBone(armature, bones.knee_gear_left).custom_shape(shapes.get("Cube"), color="THEME08", scale=(1,1,1))
        LegacyBoner.PoseBone(armature, bones.knee_gear_right).custom_shape(shapes.get("Cube"), color="THEME08", scale=(1,1,1))
        LegacyBoner.PoseBone(armature, bones.shield_left).custom_shape(shapes.get("Cube"), color="THEME08", scale=(.1,.7,1))
        LegacyBoner.PoseBone(armature, bones.shield_right).custom_shape(shapes.get("Cube"), color="THEME08", scale=(.1,.7,1))
        LegacyBoner.PoseBone(armature, bones.back_gear_left).custom_shape(shapes.get("Cube"), color="THEME08", scale=(1,2,.5))
        LegacyBoner.PoseBone(armature, bones.back_gear_right).custom_shape(shapes.get("Cube"), color="THEME08", scale=(1,2,.5))

        # Tail Bones
        for bone_name in bones.tail:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME01", scale=(3,3,1), rotation=(math.radians(-90), 0, 0))
        
        # Boob Bones
        LegacyBoner.PoseBone(armature, bones.boob_left).custom_shape(shapes.get("Circle"), color="THEME13",
                                                                scale=(.4,1,.4), translation=(0,0.2,0))
        LegacyBoner.PoseBone(armature, bones.boob_right).custom_shape(shapes.get("Circle"), color="THEME13",
                                                                scale=(.4,1,.4), translation=(0,0.2,0))

        # Torso Bones
        LegacyBoner.PoseBone(armature, bones.pelvis).custom_shape(shapes.get("Circle"), color="THEME04", scale=(1.4,1,1.4), translation=(0,0.01,0))
        LegacyBoner.PoseBone(armature, bones.abdomen).custom_shape(shapes.get("Circle"), color="THEME01", scale=(1,1,1), translation=(0,0.01,0))
        LegacyBoner.PoseBone(armature, bones.chest).custom_shape(shapes.get("Circle"), color="THEME01", scale=(1.5,1,1.5))
        LegacyBoner.PoseBone(armature, bones.upper_chest).custom_shape(shapes.get("Circle"), color="THEME01", scale=(3,1,3))
        LegacyBoner.PoseBone(armature, bones.shoulder_blade_left).custom_shape(shapes.get("Shoulder"),
            color="THEME03", scale=(0.3,-0.3,0.3), translation=(0,0.04,0), rotation=(0, math.radians(90), 0))
        LegacyBoner.PoseBone(armature, bones.shoulder_blade_right).custom_shape(shapes.get("Shoulder"),
            color="THEME03",scale=(0.3,-0.3,0.3), translation=(0,0.04,0), rotation=(0, math.radians(90), 0))

        # Neck Bones
        LegacyBoner.PoseBone(armature, bones.neck).custom_shape(shapes.get("Neck"), color="THEME01", scale=(.5,1,.5), rotation=(math.radians(90), 0, 0))
        LegacyBoner.PoseBone(armature, bones.head).custom_shape(shapes.get("Sphere"), color="THEME01", scale=(2,2,2))

        # Leg Bones
        LegacyBoner.PoseBone(armature, bones.foot_left).custom_shape(shapes.get("Ankle"), color="THEME09", scale=(1,1,1))
        LegacyBoner.PoseBone(armature, bones.toes_left).custom_shape(shapes.get("Circle"), color="THEME09", scale=(.3,1,.3),
                                                                translation=(0,0,-0.02))
        LegacyBoner.PoseBone(armature, bones.foot_right).custom_shape(shapes.get("Ankle"), color="THEME09", scale=(1,1,1))
        LegacyBoner.PoseBone(armature, bones.toes_right).custom_shape(shapes.get("Circle"), color="THEME09", scale=(.3,1,.3),
                                                                translation=(0,0,-0.02))

        # Cloth Bones
        for bone_name in bones.cloth_back_left:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))

        for bone_name in bones.cloth_front_left:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))

        for bone_name in bones.cloth_side_left:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))
        
        for bone_name in bones.cloth_back_right:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))

        for bone_name in bones.cloth_front_right:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))

        for bone_name in bones.cloth_side_right:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))


        # Setup IK Bones
        foot_ik_head_l = LegacyBoner.PoseBone(armature, bones.calf_left).getTailPos();
        foot_pole_head_l = LegacyBoner.PoseBone(armature, bones.knee_left).getTailPos() + mathutils.Vector((0,-.15,0));
        foot_ik_head_r = LegacyBoner.PoseBone(armature, bones.calf_right).getTailPos();
        foot_pole_head_r = LegacyBoner.PoseBone(armature, bones.knee_right).getTailPos() + mathutils.Vector((0,-.15,0));
        
        wrist_ik_head_l = LegacyBoner.PoseBone(armature, bones.elbow_left).getTailPos() + mathutils.Vector((0, 0, 0));
        wrist_pole_head_l = LegacyBoner.PoseBone(armature, bones.shoulder_left).getTailPos() + mathutils.Vector((0,.15,0));
        wrist_ik_head_r = LegacyBoner.PoseBone(armature, bones.elbow_right).getTailPos() + mathutils.Vector((0, 0, 0));
        wrist_pole_head_r = LegacyBoner.PoseBone(armature, bones.shoulder_right).getTailPos() + mathutils.Vector((0,.15,0));

        LegacyBoner.EditBone(armature).create(bones.IK_foot_l,head_pos=foot_ik_head_l, tail_dir=(0,0,-.05), parent_name=bones.root)
        LegacyBoner.EditBone(armature).create(bones.POLE_foot_l, head_pos=foot_pole_head_l, tail_dir=(0,-.2,0), parent_name=bones.IK_foot_l)
        LegacyBoner.PoseBone(armature, bones.calf_left).addIKConstraint(bones.IK_foot_l, pole_bone_name=bones.POLE_foot_l, chain_count=3, pole_angle=-90)
        LegacyBoner.PoseBone(armature, bones.IK_foot_l).custom_shape(shapes.get("Circle"), color="THEME07")
        LegacyBoner.PoseBone(armature, bones.POLE_foot_l).custom_shape(shapes.get("Sphere"), color="THEME06", scale=(.2,.2,.2))

        LegacyBoner.EditBone(armature).create(bones.IK_foot_r,head_pos=foot_ik_head_r, tail_dir=(0,0,-.05), parent_name=bones.root)
        LegacyBoner.EditBone(armature).create(bones.POLE_foot_r, head_pos=foot_pole_head_r, tail_dir=(0,-.2,0), parent_name=bones.IK_foot_r)
        LegacyBoner.PoseBone(armature, bones.calf_right).addIKConstraint(bones.IK_foot_r, pole_bone_name=bones.POLE_foot_r, chain_count=3, pole_angle=-90)
        LegacyBoner.PoseBone(armature, bones.IK_foot_r).custom_shape(shapes.get("Circle"), color="THEME07")
        LegacyBoner.PoseBone(armature, bones.POLE_foot_r).custom_shape(shapes.get("Sphere"), color="THEME06", scale=(.2,.2,.2))

        LegacyBoner.EditBone(armature).create(bones.IK_wrist_l,head_pos=wrist_ik_head_l, tail_dir=(.2,0,-.2), parent_name=bones.root, roll=math.radians(-45))
        LegacyBoner.EditBone(armature).create(bones.POLE_wrist_l, head_pos=wrist_pole_head_l, tail_dir=(0,.2,0), parent_name=bones.IK_wrist_l)
        LegacyBoner.PoseBone(armature, bones.elbow_left).addIKConstraint(bones.IK_wrist_l, pole_bone_name=bones.POLE_wrist_l, chain_count=2, pole_angle=90)
        LegacyBoner.PoseBone(armature, bones.wrist_left).addCopyRotationConstraint(bones.IK_wrist_l)
        LegacyBoner.PoseBone(armature, bones.IK_wrist_l).custom_shape(shapes.get("Handshape"), color="THEME06", scale=(.2,.2,.2), translation=(0,.08,0), rotation=(0, math.radians(90), 0))
        LegacyBoner.PoseBone(armature, bones.POLE_wrist_l).custom_shape(shapes.get("Sphere"), color="THEME06", scale=(.2,.2,.2))

        LegacyBoner.EditBone(armature).create(bones.IK_wrist_r,head_pos=wrist_ik_head_r, tail_dir=(-.2,0,-.2), parent_name=bones.root, roll=math.radians(45))
        LegacyBoner.EditBone(armature).create(bones.POLE_wrist_r, head_pos=wrist_pole_head_r, tail_dir=(0,.2,0), parent_name=bones.IK_wrist_r)
        LegacyBoner.PoseBone(armature, bones.elbow_right).addIKConstraint(bones.IK_wrist_r, pole_bone_name=bones.POLE_wrist_r, chain_count=2, pole_angle=90)
        LegacyBoner.PoseBone(armature, bones.wrist_right).addCopyRotationConstraint(bones.IK_wrist_r)
        LegacyBoner.PoseBone(armature, bones.IK_wrist_r).custom_shape(shapes.get("Handshape"), color="THEME06", scale=(.2,.2,.2), translation=(0,.08,0), rotation=(0, math.radians(-90), 0))
        LegacyBoner.PoseBone(armature, bones.POLE_wrist_r).custom_shape(shapes.get("Sphere"), color="THEME06", scale=(.2,.2,.2))
        

        # Face Bones
        # Jaw
        LegacyBoner.PoseBone(armature, bones.jaw).custom_shape(shapes.get("Jaw"), color="THEME03", translation=(-.03,.04,0), rotation=(0, math.radians(90), 0))
        # Lips
        LegacyBoner.PoseBone(armature, bones.corner_lip_right).custom_shape(shapes.get("Circle"), color="THEME03", scale=(.5,.5,.5),
                                                                      translation=(.07,0,0), rotation=(math.radians(-60),math.radians(90), 0))
        LegacyBoner.PoseBone(armature, bones.corner_lip_left).custom_shape(shapes.get("Circle"), color="THEME03", scale=(.5,.5,.5),
                                                                      translation=(.07,0,0), rotation=(math.radians(-60),math.radians(90), 0))

        LegacyBoner.PoseBone(armature, bones.mouth_upper).custom_shape(shapes.get("Top_Lip_In"), color="THEME03",
                scale=(.8,.8,.8), translation=(0,.055, 0), rotation=(math.radians(-60), math.radians(180), 0))
        LegacyBoner.PoseBone(armature, bones.mouth_bottom).custom_shape(shapes.get("Bottom_Lip_In"), color="THEME03",
                scale=(.8,.8,.8), translation=(0,.052, .002), rotation=(math.radians(-45), math.radians(180), 0))
        LegacyBoner.PoseBone(armature, bones.lip_upper).custom_shape(shapes.get("Top_Lip_Out"), color="THEME03",
                scale=(1,1,1), translation=(0,.009, .002), rotation=(math.radians(-45), 0, 0))
        LegacyBoner.PoseBone(armature, bones.lip_bottom).custom_shape(shapes.get("Bottom_Lip_Out"), color="THEME03",
                scale=(1,1,1), translation=(0,.009, -.002), rotation=(math.radians(-45), 0, 0))

        # Cheeks
        LegacyBoner.PoseBone(armature, bones.cheek_left).custom_shape(shapes.get("Circle"), color="THEME03", translation=(.1,0,0),
                                                                rotation=(math.radians(90), math.radians(90), 0))
        LegacyBoner.PoseBone(armature, bones.cheek_right).custom_shape(shapes.get("Circle"), color="THEME03", translation=(.1,0,0),
                                                                rotation=(math.radians(90), math.radians(90), 0))

        # Nose
        LegacyBoner.PoseBone(armature, bones.nose).custom_shape(shapes.get("Circle"), color="THEME03", scale=(.5,.5,.5),
                                                          translation=(.1,0,0), rotation=(math.radians(90), math.radians(90), 0))

        # Eyes
        LegacyBoner.PoseBone(armature, bones.eyelid_left_bottom).custom_shape(shapes.get("Eyelid_Bottom"), color="THEME03",
                scale=(15,15,15), translation=(.02,0,0), rotation=(math.radians(180), math.radians(90),0))
        LegacyBoner.PoseBone(armature, bones.eyelid_right_bottom).custom_shape(shapes.get("Eyelid_Bottom"), color="THEME03",
                scale=(15,15,15), translation=(.02,0,0), rotation=(math.radians(180), math.radians(90),0))
        
        LegacyBoner.PoseBone(armature, bones.eyelid_left_top).custom_shape(shapes.get("Eyelid_top"), color="THEME03",
                scale=(15,15,15), translation=(.02,0,0), rotation=(math.radians(180), math.radians(-90),0))
        LegacyBoner.PoseBone(armature, bones.eyelid_right_top).custom_shape(shapes.get("Eyelid_top"), color="THEME03",
                scale=(15,15,15), translation=(.02,0,0), rotation=(math.radians(180), math.radians(-90),0))

        # Eyebrows
        LegacyBoner.PoseBone(armature, bones.eyebrow_left_main).custom_shape(shapes.get("Circle"), color="THEME03",
                scale=(.7,.7,.7), translation=(.11,0,-.01), rotation=(math.radians(-60), math.radians(90), 0))
        LegacyBoner.PoseBone(armature, bones.eyebrow_left_inner).custom_shape(shapes.get("Circle"), color="THEME03",
                scale=(.5,.5,.5), translation=(.08,0,0), rotation=(math.radians(-60), math.radians(90), 0))
        LegacyBoner.PoseBone(armature, bones.eyebrow_right_main).custom_shape(shapes.get("Circle"), color="THEME03",
                scale=(.7,.7,.7), translation=(.11,0,.01), rotation=(math.radians(-60), math.radians(90), 0))
        LegacyBoner.PoseBone(armature, bones.eyebrow_right_inner).custom_shape(shapes.get("Circle"), color="THEME03",
                scale=(.5,.5,.5), translation=(.08,0,0), rotation=(math.radians(-60), math.radians(90), 0))

        # Hair Bones
        for bone_name in bones.hair_long:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))

        LegacyBoner.PoseBone(armature, bones.hair_back).custom_shape(shapes.get("Sphere"), color="THEME07")
        LegacyBoner.PoseBone(armature, bones.hair_left).custom_shape(shapes.get("Sphere"), color="THEME07")
        LegacyBoner.PoseBone(armature, bones.hair_right).custom_shape(shapes.get("Sphere"), color="THEME07")
        LegacyBoner.PoseBone(armature, bones.hair_front).custom_shape(shapes.get("Sphere"), color="THEME07")
        LegacyBoner.PoseBone(armature, bones.hair_extensions_left).custom_shape(shapes.get("Sphere"), color="THEME07")
        LegacyBoner.PoseBone(armature, bones.hair_extensions_right).custom_shape(shapes.get("Sphere"), color="THEME07")

        # Ear & Earring
        LegacyBoner.PoseBone(armature, bones.ear_left).custom_shape(shapes.get("Sphere"), color="THEME01", scale=(.1,.1,.1))
        LegacyBoner.PoseBone(armature, bones.ear_right).custom_shape(shapes.get("Sphere"), color="THEME01", scale=(.1,.1,.1))

        for bone_name in bones.earring_left:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))
        for bone_name in bones.earring_right:
            LegacyBoner.PoseBone(armature, bone_name).custom_shape(shapes.get("Arrow"), color="THEME07", rotation=(math.radians(-90), 0, 0))


        # Disable Inherit Rotation on feet
        LegacyBoner.PoseBone(armature, bones.foot_left).disableInheritRotation()
        LegacyBoner.PoseBone(armature, bones.foot_right).disableInheritRotation()

        # # Hide Unused Bones
        LegacyBoner.PoseBone(armature, "n_throw").visibility(False)
        LegacyBoner.PoseBone(armature, bones.tail_extra).visibility(False)

        # - Leg FK
        LegacyBoner.PoseBone(armature, bones.thigh_left).visibility(False)
        LegacyBoner.PoseBone(armature, bones.knee_left).visibility(False)
        LegacyBoner.PoseBone(armature, bones.calf_left).visibility(False)
        LegacyBoner.PoseBone(armature, bones.thigh_right).visibility(False)
        LegacyBoner.PoseBone(armature, bones.knee_right).visibility(False)
        LegacyBoner.PoseBone(armature, bones.calf_right).visibility(False)

        # - Arm FK
        LegacyBoner.PoseBone(armature, bones.wrist_left).visibility(False)
        LegacyBoner.PoseBone(armature, bones.elbow_left).visibility(False)
        LegacyBoner.PoseBone(armature, bones.shoulder_left).visibility(False)
        LegacyBoner.PoseBone(armature, bones.wrist_right).visibility(False)
        LegacyBoner.PoseBone(armature, bones.elbow_right).visibility(False)
        LegacyBoner.PoseBone(armature, bones.shoulder_right).visibility(False)

        return {'FINISHED'}
    
