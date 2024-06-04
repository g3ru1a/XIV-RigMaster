import bpy
from .utils.config import config
from .panels import legacy_panel, steps_panel

from .operators import TestOperator
from .operators.legacy import toggle_visibility_operators as tvo
from .operators.legacy import custom_shapes_operator as cso
from .operators.legacy import pose_reset_operator as pro


bl_info = {
    "name": config.name,
    "id_name": config.id_name,
    "author": config.author,
    "version": config.version,
    "blender": config.blender,
    "location": config.location,
    "description": config.description,
    "warning": "",
    "doc_url": "",
    "category": config.category,
}


def register():
    bpy.utils.register_class(TestOperator.TestOperator)
    
    # Dawntrail Functionality
    # bpy.utils.register_class(steps_panel.VIEW3D_PT_StepsPanel)

    # Legacy Functionality
    bpy.utils.register_class(legacy_panel.VIEW3D_PT_LegacyPanel)

    bpy.utils.register_class(cso.ARMATURE_OT_CustomShapes)
    bpy.utils.register_class(pro.ARMATURE_OT_PoseReset)

    bpy.utils.register_class(tvo.ARMATURE_OT_ToggleClothes)
    bpy.utils.register_class(tvo.ARMATURE_OT_ToggleFace)
    bpy.utils.register_class(tvo.ARMATURE_OT_ToggleGear)
    bpy.utils.register_class(tvo.ARMATURE_OT_ToggleHair)
    bpy.utils.register_class(tvo.ARMATURE_OT_ToggleTwist)
    bpy.utils.register_class(tvo.ARMATURE_OT_ToggleTail)

def unregister():
    bpy.utils.unregister_class(TestOperator.TestOperator)

    # Dawntrail Functionality
    # bpy.utils.unregister_class(steps_panel.VIEW3D_PT_StepsPanel)

    # Legacy Functionality
    bpy.utils.unregister_class(legacy_panel.VIEW3D_PT_LegacyPanel)

    bpy.utils.unregister_class(cso.ARMATURE_OT_CustomShapes)
    bpy.utils.unregister_class(pro.ARMATURE_OT_PoseReset)

    bpy.utils.unregister_class(tvo.ARMATURE_OT_ToggleClothes)
    bpy.utils.unregister_class(tvo.ARMATURE_OT_ToggleFace)
    bpy.utils.unregister_class(tvo.ARMATURE_OT_ToggleGear)
    bpy.utils.unregister_class(tvo.ARMATURE_OT_ToggleHair)
    bpy.utils.unregister_class(tvo.ARMATURE_OT_ToggleTwist)
    bpy.utils.unregister_class(tvo.ARMATURE_OT_ToggleTail)
    

if __name__ == "__main__":
    register()    