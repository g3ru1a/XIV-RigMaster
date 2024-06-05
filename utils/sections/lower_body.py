import math
from ..section import Section
from ..tools import mode_set, import_shape_collection
from ..config import config
from .. import bones

class Waist(Section):
    bones = [bones.pelvis, bones.waist]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            hip = self.armature.get_bone(bones.pelvis)
            waist = self.armature.get_bone(bones.waist)

            hip.set_custom_shape(shapes.get("Hip"), scale=(.4, .4, .4))
            hip.set_custom_shape_offset(offset=(0,.035, 0))
            hip.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))
            hip.set_custom_shape_color(color="THEME01")

            waist.set_custom_shape(shapes.get("Waist"), scale=(18,25,25))
            waist.set_custom_shape_offset(offset=(-.08,0, 0))
            waist.set_custom_shape_rotation(rotation=(math.radians(90), 0, math.radians(90)))
            waist.set_custom_shape_color(color="THEME03")

class LeftLeg(Section):
    bones = [bones.thigh_left, bones.knee_left, bones.calf_left, bones.foot_left, bones.toes_left]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            
            thigh = self.armature.get_bone(bones.thigh_left)
            thigh.set_custom_shape(shapes.get("Cylinder"), scale=(.15,.15,.5))
            thigh.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))
            
            calf = self.armature.get_bone(bones.calf_left)
            calf.set_custom_shape(shapes.get("Cylinder"), scale=(.1,.1,.55))
            calf.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))
            calf.set_custom_shape_offset(offset=(.01, -.02, 0))

            knee = self.armature.get_bone(bones.knee_left)
            knee.set_custom_shape(shapes.get("Sphere"))
            knee.set_custom_shape_color(color="THEME02")

            foot = self.armature.get_bone(bones.foot_left)
            foot.set_custom_shape(shapes.get("Sphere"), scale=(.3,.3,.3))
            foot.set_custom_shape_color(color="THEME02")

            toes = self.armature.get_bone(bones.toes_left)
            toes.set_custom_shape(shapes.get("Circle"), scale=(.2,.4,1))
            toes.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))

            for bone_name in [bones.thigh_left, bones.calf_left, bones.toes_left]:
                bone = self.armature.get_bone(bone_name)
                bone.set_custom_shape_color(color="THEME01")

class RightLeg(Section):
    bones = [bones.thigh_right, bones.knee_right, bones.calf_right, bones.foot_right, bones.toes_right]

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            
            thigh = self.armature.get_bone(bones.thigh_right)
            thigh.set_custom_shape(shapes.get("Cylinder"), scale=(.15,.15,.5))
            thigh.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))
            
            calf = self.armature.get_bone(bones.calf_right)
            calf.set_custom_shape(shapes.get("Cylinder"), scale=(.1,.1,.55))
            calf.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))
            calf.set_custom_shape_offset(offset=(.01, -.02, 0))

            knee = self.armature.get_bone(bones.knee_right)
            knee.set_custom_shape(shapes.get("Sphere"))
            knee.set_custom_shape_color(color="THEME02")

            foot = self.armature.get_bone(bones.foot_right)
            foot.set_custom_shape(shapes.get("Sphere"), scale=(.3,.3,.3))
            foot.set_custom_shape_color(color="THEME02")

            toes = self.armature.get_bone(bones.toes_right)
            toes.set_custom_shape(shapes.get("Circle"), scale=(.2,.4,1))
            toes.set_custom_shape_rotation(rotation=(math.radians(90), 0, 0))

            for bone_name in [bones.thigh_right, bones.calf_right, bones.toes_right]:
                bone = self.armature.get_bone(bone_name)
                bone.set_custom_shape_color(color="THEME01")

class Legs(Section):
    bones = LeftLeg.bones + RightLeg.bones

    def setup(self) -> None:
        LeftLeg(self.armature).setup()
        RightLeg(self.armature).setup()

class Tail(Section):
    bones = bones.tail

    def setup(self) -> None:
        shapes = import_shape_collection(config.custom_shapes_filename)
        with mode_set(mode="POSE"):
            for bone_name in self.bones:
                bone = self.armature.get_bone(bone_name)
                if bone is not None:
                    bone.set_custom_shape(shapes.get("Circle"), scale=(.3,.3,1))
                    bone.set_custom_shape_rotation(rotation=(math.radians(90),0,0))
                    bone.set_custom_shape_color(color="THEME07")