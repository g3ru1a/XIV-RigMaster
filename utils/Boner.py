from typing import Tuple
import bpy, mathutils, math

class PoseBone:
    armature: bpy.types.Armature
    bone: bpy.types.PoseBone

    def __init__(self, armature: bpy.types.Armature, bone_name: str) -> None:
        self.armature = armature;
        self.bone = armature.pose.bones.get(bone_name)
        if(self.bone is None):
            raise ValueError(f"Value Error: {bone_name} not found in the armature.")
    
    def custom_shape(self, custom_object: bpy.types.Object, color: str="DEFAULT", scale=(1,1,1),
                    translation=(0,0,0), rotation=(0,0,0)) -> None:
        bpy.ops.object.mode_set(mode="POSE")
        self.bone.custom_shape = custom_object
        self.bone.custom_shape_scale_xyz = scale
        self.bone.custom_shape_translation = translation
        self.bone.custom_shape_rotation_euler = mathutils.Euler(rotation, "XYZ")
        self.bone.color.palette = color
        bpy.ops.object.mode_set(mode="OBJECT")

    def visibility(self, visible: bool):
        bpy.ops.object.mode_set(mode="POSE")
        self.bone.bone.hide = not visible
        bpy.ops.object.mode_set(mode="OBJECT")

    def toggleVisibility(self) -> None:
        bpy.ops.object.mode_set(mode="POSE")
        self.bone.bone.hide = not self.bone.bone.hide;
        bpy.ops.object.mode_set(mode="OBJECT")

    def getTailPos(self) -> Tuple[float,float,float] | mathutils.Vector:
        return self.bone.tail
    
    def getHeadPos(self) -> Tuple[float,float,float] | mathutils.Vector:
        return self.bone.head
    
    def addIKConstraint(self, bone_name: str, chain_count: int = 1, pole_bone_name: str = None, pole_angle: float = 0) -> None:
        # Retrieve the target object that will act as the IK controller
        target = bpy.data.objects.get(self.armature.name)
        if not target:
            raise ValueError(f"Target object '{self.armature.name}' not found.")
        bpy.ops.object.mode_set(mode='POSE')
        ik_constraint: bpy.types.KinematicConstraint = self.bone.constraints.new(type="IK")
        ik_constraint.target = target
        ik_constraint.subtarget = bone_name
        if pole_bone_name is not None:
            ik_constraint.pole_target = target
            ik_constraint.pole_subtarget = pole_bone_name
            ik_constraint.pole_angle = math.radians(pole_angle);
        ik_constraint.chain_count = chain_count
        bpy.ops.object.mode_set(mode='OBJECT')
    
    def addCopyRotationConstraint(self, bone_name: str) -> None:
        target = bpy.data.objects.get(self.armature.name)
        if not target:
            raise ValueError(f"Target object '{self.armature.name}' not found.")
        bpy.ops.object.mode_set(mode='POSE')
        cr_constraint: bpy.types.CopyRotationConstraint = self.bone.constraints.new(type="COPY_ROTATION")
        cr_constraint.target = target
        cr_constraint.subtarget = bone_name
        cr_constraint.target_space = "POSE"
        cr_constraint.owner_space = "POSE"
        bpy.ops.object.mode_set(mode='OBJECT')

    def disableInheritRotation(self) -> None:
        bpy.ops.object.mode_set(mode='POSE')
        self.bone.bone.use_inherit_rotation = False
        bpy.ops.object.mode_set(mode='OBJECT')

class EditBone:
    armature: bpy.types.Object
    bone: bpy.types.EditBone

    def __init__(self, armature: bpy.types.Object) -> None:
        self.armature = armature
       
    def create(self, bone_name: str, head_pos=(0,0,0), tail_dir=(0,1,0),
                    parent_name: str=None, roll: float = math.radians(0)) -> None:
        bpy.ops.object.mode_set(mode='EDIT')
        edit_bones: bpy.types.ArmatureEditBones = self.armature.data.edit_bones
        if bone_name in edit_bones:
            self.bone = self.armature.data.edit_bones.get(bone_name)
        else:
            bone: bpy.types.EditBone = edit_bones.new(bone_name)
            bone.head = head_pos
            bone.tail = head_pos + mathutils.Vector(tail_dir)
            bone.roll = roll
            if parent_name and parent_name in edit_bones:
                bone.parent = edit_bones[parent_name]
            self.bone = bone
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.update()
    
    def find(self, bone_name: str) -> None:
        bpy.ops.object.mode_set(mode='EDIT')
        self.bone = self.armature.data.edit_bones.get(bone_name)
        bpy.ops.object.mode_set(mode='OBJECT')

    def getTailPos(self) -> Tuple[float,float,float] | mathutils.Vector:
        return self.bone.tail
    
    def getHeadPos(self) -> Tuple[float,float,float] | mathutils.Vector:
        return self.bone.head

    def tail2head(armature: bpy.types.Object, bone1_name: str, bone2_name: str) -> None:
        bpy.ops.object.mode_set(mode='EDIT')
    
        # Access the bones in Edit Mode
        edit_bones = armature.data.edit_bones
        bone1 = edit_bones.get(bone1_name)
        bone2 = edit_bones.get(bone2_name)

        if not bone1:
            raise ValueError(f"Bone '{bone1_name}' not found in armature '{armature}'.")
        if not bone2:
            raise ValueError(f"Bone '{bone2_name}' not found in armature '{armature}'.")

        # Align the tail of bone1 to the head of bone2
        bone1.tail = bone2.head

        # Optionally switch back to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')