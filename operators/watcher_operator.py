import bpy

class OBJECT_OT_ArmatureSelectWatcher(bpy.types.Operator):
    """Operator to watch for armature selection"""
    bl_idname = "xivrm.armature_select_watcher"
    bl_label = "Armature Select Watcher"
    bl_options = {'REGISTER', 'UNDO'}

    _timer = None
    _last_active_object = None

    def modal(self, context, event):
        if event.type == 'TIMER':
            current_active_object = context.view_layer.objects.active
            if current_active_object != self._last_active_object:
                self._last_active_object = current_active_object
                if current_active_object and current_active_object.type == 'ARMATURE':
                    self.on_armature_selected(current_active_object)

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(1.0, window=context.window)
        wm.modal_handler_add(self)
        self._last_active_object = context.view_layer.objects.active
        return {'RUNNING_MODAL'}

    def on_armature_selected(self, armature):
        # Your custom code to run when an armature is selected
        self.report({'INFO'}, f"Selected armature: {armature.name}")

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        return {'CANCELLED'}