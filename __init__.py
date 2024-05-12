bl_info = {
    "name": "XIV Bone Cleaner",
    "id_name": "xivbc",
    "author": "G3ru1a",
    "version": (0, 1),
    "blender": (4, 0, 0),
    "location": "View3D > UI > XIV Bone Cleaner",
    "description": "Cleans up the bones from a Meddle Exported .gltf Model",
    "warning": "",
    "doc_url": "",
    "category": "XIV Bone Cleaner 0.2",
}


import bpy
from . import XIVBoneCleaner as xivbc;
from .operators import BoneCleanup, ArmatureFixer, TestOperator
from .operators import ToggleBones


def register():
    bpy.utils.register_class(xivbc.XIVBCMainPanel)
    bpy.utils.register_class(BoneCleanup.BoneRemovalOperator)
    bpy.utils.register_class(ArmatureFixer.ArmatureFixerOperator)
    bpy.utils.register_class(TestOperator.TestOperator)
    bpy.utils.register_class(ToggleBones.ToggleClothes_OP)
    bpy.utils.register_class(ToggleBones.ToggleFace_OP)
    bpy.utils.register_class(ToggleBones.ToggleGear_OP)
    bpy.utils.register_class(ToggleBones.ToggleHair_OP)
    bpy.utils.register_class(ToggleBones.ToggleTwist_OP)
    bpy.utils.register_class(ToggleBones.ToggleTail_OP)

def unregister():
    bpy.utils.unregister_class(xivbc.XIVBCMainPanel)
    bpy.utils.unregister_class(BoneCleanup.BoneRemovalOperator)
    bpy.utils.unregister_class(ArmatureFixer.ArmatureFixerOperator)
    bpy.utils.unregister_class(TestOperator.TestOperator)
    bpy.utils.unregister_class(ToggleBones.ToggleClothes_OP)
    bpy.utils.unregister_class(ToggleBones.ToggleFace_OP)
    bpy.utils.unregister_class(ToggleBones.ToggleGear_OP)
    bpy.utils.unregister_class(ToggleBones.ToggleHair_OP)
    bpy.utils.unregister_class(ToggleBones.ToggleTwist_OP)
    bpy.utils.unregister_class(ToggleBones.ToggleTail_OP)
    

if __name__ == "__main__":
    register()    