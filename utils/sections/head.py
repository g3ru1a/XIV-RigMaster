import math
from ..section import Section
from ..tools import mode_set, import_shape_collection
from ..config import data as config
from .. import bones

class Head(Section):
    bones = [bones.head]

    def setup(self) -> None:
        shapes = import_shape_collection(config["custom_shapes_filename"])
        with mode_set(mode="POSE"):
            head = self.armature.get_bone(bones.head)

            head.set_custom_shape(shapes.get("CurvedArrow"), scale=(1.2,1.2,3.2))
            head.set_custom_shape_offset(offset=(-.04,-.02,0))
            head.set_custom_shape_rotation(rotation=(math.radians(90), math.radians(-45), math.radians(-20)))
            head.set_custom_shape_color(color="THEME06")

class Neck(Section):
    bones = [bones.neck]

    def setup(self) -> None:
        shapes = import_shape_collection(config["custom_shapes_filename"])
        with mode_set(mode="POSE"):
            head = self.armature.get_bone(bones.neck)

            head.set_custom_shape(shapes.get("CurvedArrow"), scale=(.6,.6,1))
            head.set_custom_shape_offset(offset=(0,.02,0))
            head.set_custom_shape_rotation(rotation=(math.radians(90), math.radians(-45), 0))
            head.set_custom_shape_color(color="THEME06")

