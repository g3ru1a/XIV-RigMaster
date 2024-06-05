import bpy

from .utils.config import data as config
from .utils.tools import get_addon_absolute_path, all_operators_in_module

from .panels import armature_controls_panel, legacy_panel, steps_panel
from .panels.armature_controls_panel import VisibilityProperties
from .panels.steps_panel import StepsProperties
from .panels.dev_panel import VIEW3D_PT_DevPanel, DevProperties

from .operators.legacy import toggle_visibility_operators as tvo
from .operators.legacy import custom_shapes_operator as cso
from .operators.legacy import pose_reset_operator as pro

from .operators import custom_shapes_operator
from .operators import visibility_operators as VO
from .operators import dev_operators

bl_info = {
    "name": config["name"],
    "id_name": config["id_name"],
    "author": config["author"],
    "version": config["version"],
    "blender": config["blender"],
    "location": config["location"],
    "description": config["description"],
    "warning": "",
    "doc_url": "",
    "category": config["category"],
}

# Property to store the last active object
# bpy.types.Scene.last_active_object = bpy.props.PointerProperty(type=bpy.types.Object)

# def armature_selection_handler(scene):
#     current_active_object = bpy.context.view_layer.objects.active
#     if current_active_object != scene.last_active_object:
#         scene.last_active_object = current_active_object
#         if current_active_object and current_active_object.type == 'ARMATURE':
#             on_armature_selected(current_active_object)

# def on_armature_selected(armature):
#     # Your custom code to run when an armature is selected
#     print(f"Selected armature: {armature.name}")

def register():
    # Listener
    # bpy.app.handlers.depsgraph_update_post.append(armature_selection_handler)

    # Development
    if config["production"] is False:
        bpy.utils.register_class(DevProperties)
        bpy.types.Scene.dev_props = bpy.props.PointerProperty(type=DevProperties)
        bpy.utils.register_class(VIEW3D_PT_DevPanel)
        all_operators_in_module(dev_operators, register=True)

    # Dawntrail Functionality
    ## Props
    bpy.utils.register_class(VisibilityProperties)
    bpy.types.Scene.visibility_props = bpy.props.PointerProperty(type=VisibilityProperties)
    bpy.utils.register_class(StepsProperties)
    bpy.types.Scene.steps_props = bpy.props.PointerProperty(type=StepsProperties)

    ## Panels
    bpy.utils.register_class(steps_panel.VIEW3D_PT_StepsPanel)
    bpy.utils.register_class(armature_controls_panel.VIEW3D_PT_ControlsPanel)

    ## Operators
    bpy.utils.register_class(custom_shapes_operator.ARMATURE_OT_CustomShapes)
    all_operators_in_module(VO, register=True)

    # Legacy Functionality
    bpy.utils.register_class(legacy_panel.VIEW3D_PT_LegacyPanel)
    bpy.utils.register_class(cso.ARMATURE_OT_CustomShapes)
    bpy.utils.register_class(pro.ARMATURE_OT_PoseReset)
    all_operators_in_module(tvo, register=True)

def unregister():
    # Listener
    # bpy.app.handlers.depsgraph_update_post.remove(armature_selection_handler)
    # del bpy.types.Scene.last_active_object

    # Development
    if config["production"] is False:
        bpy.utils.unregister_class(DevProperties)
        del bpy.types.Scene.dev_props
        bpy.utils.unregister_class(VIEW3D_PT_DevPanel)
        all_operators_in_module(dev_operators, register=False)

    # Dawntrail Functionality
    ## Props
    bpy.utils.unregister_class(VisibilityProperties)
    del bpy.types.Scene.visibility_props
    bpy.utils.unregister_class(StepsProperties)
    del bpy.types.Scene.steps_props

    ## Panels
    bpy.utils.unregister_class(steps_panel.VIEW3D_PT_StepsPanel)
    bpy.utils.unregister_class(armature_controls_panel.VIEW3D_PT_ControlsPanel)

    ## Operators
    bpy.utils.unregister_class(custom_shapes_operator.ARMATURE_OT_CustomShapes)
    all_operators_in_module(VO, register=False)

    # Legacy Functionality
    bpy.utils.unregister_class(legacy_panel.VIEW3D_PT_LegacyPanel)
    bpy.utils.unregister_class(cso.ARMATURE_OT_CustomShapes)
    bpy.utils.unregister_class(pro.ARMATURE_OT_PoseReset)
    all_operators_in_module(tvo, register=False)
    

if __name__ == "__main__":
    register()
    # bpy.ops.xivrm.armature_select_watcher()    