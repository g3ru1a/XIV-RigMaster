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
    "category": "XIV Bone Cleaner 0.1",
}


import bpy
from . import XIVBoneCleaner as xivbc;
from .operators import BoneCleanup, ArmatureFixer, TestOperator


def register():
    bpy.utils.register_class(xivbc.XIVBCMainPanel)
    bpy.utils.register_class(BoneCleanup.BoneRemovalOperator)
    bpy.utils.register_class(ArmatureFixer.ArmatureFixerOperator)
    bpy.utils.register_class(TestOperator.TestOperator)
    bpy.utils.register_class(xivbc.ToggleHandBones)

def unregister():
    bpy.utils.unregister_class(xivbc.XIVBCMainPanel)
    bpy.utils.unregister_class(BoneCleanup.BoneRemovalOperator)
    bpy.utils.unregister_class(ArmatureFixer.ArmatureFixerOperator)
    bpy.utils.unregister_class(TestOperator.TestOperator)
    bpy.utils.unregister_class(xivbc.ToggleHandBones)
    

if __name__ == "__main__":
    register()    