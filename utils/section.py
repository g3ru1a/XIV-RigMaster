import bpy
from .tools import mode_set
from .armature import RM_Armature

class Section:
    armature: RM_Armature = None
    bones: list = []

    def __init__(self, armature: RM_Armature) -> None:
        self.armature = armature

    def setup(self) -> None:
        return
    
    def toggle_visibility(self) -> bool:
        with mode_set(mode="POSE"):
            for bone_name in self.bones:
                bone = self.armature.get_bone(bone_name)
                if bone is not None: bone.toggle_visibility()
            bone = self.armature.get_bone(self.bones[0])
            if bone is None: return False
            return not bone.bone.bone.hide

    def hide(self) -> None:
        with mode_set(mode="POSE"):
            for bone_name in self.bones:
                bone = self.armature.get_bone(bone_name)
                if bone is not None: bone.set_visibility(visible=False)
    
