import math
from ..section import Section
from ..tools import mode_set, import_shape_collection
from ..config import config
from .. import bones

class TwistBones(Section):
    bones = [bones.forearm_twist_left, bones.forearm_twist_right, bones.shoulder_twist_left,
             bones.shoulder_twist_right, bones.upperarm_twist_left, bones.upperarm_twist_right]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            for bone_name in self.bones:
                bone = self.armature.get_bone(bone_name)
                bone.set_custom_shape(shapes.get("Sphere"), scale=(.3,.3,.3))
                bone.set_custom_shape_color(color="THEME04")

class LeftArm(Section):
    bones = [bones.wrist_left, bones.elbow_left, bones.shoulder_left]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            cone_bones = [bones.elbow_left, bones.shoulder_left]
            for bone_name in cone_bones:
                bone = self.armature.get_bone(bone_name)
                bone.set_custom_shape(shapes.get("Cylinder"), scale=(.3,.3,.8))
                bone.set_custom_shape_rotation(rotation=(math.radians(90),0,0))
                bone.set_custom_shape_color(color="THEME01")
            self.armature.get_bone(bones.elbow_left).set_custom_shape_offset(offset=(0,.03, 0))
            self.armature.get_bone(bones.shoulder_left).set_custom_shape_offset(offset=(0,.04, 0))
            
            bone = self.armature.get_bone(bones.wrist_left)
            bone.set_custom_shape(shapes.get("Circle"), scale=(.5,.5,1))
            bone.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))
            bone.set_custom_shape_color(color="THEME01")

class RightArm(Section):
    bones = [bones.wrist_right, bones.elbow_right, bones.shoulder_right]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            cone_bones = [bones.elbow_right, bones.shoulder_right]
            for bone_name in cone_bones:
                bone = self.armature.get_bone(bone_name)
                bone.set_custom_shape(shapes.get("Cylinder"), scale=(.3,.3,.8))
                bone.set_custom_shape_rotation(rotation=(math.radians(90),0,0))
                bone.set_custom_shape_color(color="THEME01")
            self.armature.get_bone(bones.elbow_right).set_custom_shape_offset(offset=(0,.03, 0))
            self.armature.get_bone(bones.shoulder_right).set_custom_shape_offset(offset=(0,.04, 0))
            
            bone = self.armature.get_bone(bones.wrist_right)
            bone.set_custom_shape(shapes.get("Circle"), scale=(.5,.5,1))
            bone.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))
            bone.set_custom_shape_color(color="THEME01")

class Arms(Section):
    bones = LeftArm.bones + RightArm.bones
    
    def setup(self) -> None:
        LeftArm(self.armature).setup()
        RightArm(self.armature).setup()

class LeftHand(Section):
    bones = bones.fingers_left

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            for bone_name in self.bones:
                bone = self.armature.get_bone(bone_name)
                bone.set_custom_shape(shapes.get("Circle"), scale=(.2,.2,.2))
                bone.set_custom_shape_rotation(rotation=(math.radians(90),0,0))
                bone.set_custom_shape_color(color="THEME09")
            self.armature.get_bone(bones.thumb_left).set_custom_shape_offset(offset=(0, .02, 0))

class RightHand(Section):
    bones = bones.fingers_right

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            for bone_name in self.bones:
                bone = self.armature.get_bone(bone_name)
                bone.set_custom_shape(shapes.get("Circle"), scale=(.2,.2,.2))
                bone.set_custom_shape_rotation(rotation=(math.radians(90),0,0))
                bone.set_custom_shape_color(color="THEME09")
            self.armature.get_bone(bones.thumb_right).set_custom_shape_offset(offset=(0, .02, 0))

class Hands(Section):
    bones = LeftHand.bones + RightHand.bones

    def setup(self) -> None:
        LeftHand(self.armature).setup()
        RightHand(self.armature).setup()

class Shoulders(Section):
    bones = [bones.shoulder_blade_left, bones.shoulder_blade_right]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            for bone_name in self.bones:
                bone = self.armature.get_bone(bone_name)
                bone.set_custom_shape(shapes.get("Shoulder"), scale=(.4,.4,.5))
                bone.set_custom_shape_rotation(rotation=(math.radians(180),math.radians(180),math.radians(80)))
                bone.set_custom_shape_offset(offset=(0,.03,0))
                bone.set_custom_shape_color(color="THEME09")

class Spine(Section):
    bones = [bones.upper_chest, bones.chest, bones.abdomen]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            chest = self.armature.get_bone(bones.upper_chest)
            abdomen_top = self.armature.get_bone(bones.chest)
            abdomen_bottom = self.armature.get_bone(bones.abdomen)

            chest.set_custom_shape(shapes.get("Waist"), scale=(1.7,2,4))
            chest.set_custom_shape_offset(offset=(.01, -.01, 0))
            chest.set_custom_shape_rotation(rotation=(math.radians(-110), math.radians(90), 0))

            abdomen_top.set_custom_shape(shapes.get("Circle"), scale=(1,1.2,1))
            abdomen_top.set_custom_shape_offset(offset=(.04,0,0))
            abdomen_top.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))

            abdomen_bottom.set_custom_shape(shapes.get("Circle"), scale=(.6, .6, 1))
            abdomen_bottom.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))
            
            chest.set_custom_shape_color(color="THEME01");
            abdomen_top.set_custom_shape_color(color="THEME01");
            abdomen_bottom.set_custom_shape_color(color="THEME01");

class Boobs(Section):
    bones = [bones.boob_left, bones.boob_right]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            for bone_name in self.bones:
                bone = self.armature.get_bone(bone_name)
                if bone is not None:
                    bone.set_custom_shape(shapes.get("Cup"), scale=(.45,.5,.5))
                    bone.set_custom_shape_rotation(rotation=(math.radians(180),0,0))
                    bone.set_custom_shape_offset(offset=(.01,.095,0))
                    bone.set_custom_shape_color(color="THEME13")