import math
from ..section import Section
from .. import bones

class Clothing(Section):
    bones = bones.cloth_back_left + bones.cloth_back_right + bones.cloth_front_left + bones.cloth_front_right + bones.cloth_side_left + bones.cloth_side_right

    def setup(self) -> None:
        return super().setup()
    
class Gear(Section):
    bones = [bones.back_gear_left, bones.back_gear_right, bones.knee_gear_left, bones.knee_gear_right,
             bones.elbow_gear_left, bones.elbow_gear_right, bones.waist_gear2_left, bones.waist_gear2_right,
             bones.waist_gear_left, bones.waist_gear_right, bones.shoulder_gear_left, bones.shoulder_gear_right,
             bones.shield_left, bones.shield_right, bones.weapon_grip_left, bones.weapon_grip_right]
    
    def setup(self) -> None:
        return super().setup()
    
class Unused(Section):
    bones = ["n_throw", bones.tail_extra]

    def setup(self) -> None:
        return super().setup()