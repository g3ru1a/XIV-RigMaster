import bpy
import mathutils
from .tools import mode_set


class RM_Bone:
    bone: bpy.types.PoseBone = None

    def __init__(self, bone: bpy.types.PoseBone) -> None:
        self.bone = bone
    
    def set_custom_shape(self, custom_object: bpy.types.Object, scale: tuple[float, float, float] = (1,1,1)) -> None:
        with mode_set(mode="POSE"):
            self.bone.custom_shape = custom_object
            self.bone.custom_shape_scale_xyz = scale
            self.bone.custom_shape_rotation_euler = mathutils.Euler((0,0,0), "XYZ")
            self.bone.custom_shape_translation = (0,0,0)
            self.bone.color.palette = "DEFAULT"
    
    def set_custom_shape_rotation(self, rotation: tuple[float,float,float] = (0, 0, 0)) -> None:
        with mode_set(mode="POSE"):
            self.bone.custom_shape_rotation_euler = mathutils.Euler(rotation, "XYZ")
    
    def set_custom_shape_rotation_euler(self, rotation: tuple[float,float,float] = (0, 0, 0)) -> None:
        with mode_set(mode="POSE"):
            self.bone.custom_shape_rotation_euler = rotation

    def set_custom_shape_offset(self, offset: tuple[float,float,float] = (0, 0, 0)) -> None:
        with mode_set(mode="POSE"):
            self.bone.custom_shape_translation = offset
    
    def set_custom_shape_color(self, color: str) -> None:
        with mode_set(mode="POSE"):
            self.bone.color.palette = color

    def set_visibility(self, visible: bool) -> None:
        with mode_set(mode="POSE"):
            self.bone.bone.hide = not visible;

    def toggle_visibility(self) -> None:
        with mode_set(mode="POSE"):
            self.bone.bone.hide = not self.bone.bone.hide;


class RM_Armature:
    armature: bpy.types.Armature = None

    def __init__(self, armature: bpy.types.Armature) -> None:
        self.armature = armature

    def get_bone(self, bone_name: str) -> RM_Bone | None:
        if bone_name is None: return;
        bone = self.armature.pose.bones.get(bone_name)
        if bone is None:
            return None
        return RM_Bone(bone);

    


