import bpy
from ...utils.config import config
from ...utils.armature import RM_Armature
from ...utils.sections.upper_body import TwistBones, Arms, Hands, Shoulders, Spine, Boobs
from ...utils.sections.lower_body import Waist, Legs, Tail
from ...utils.sections.head import Head, Neck
from ...utils.sections.extras import Gear, Clothing, Unused

class ARMATURE_OT_CustomShapes(bpy.types.Operator):
    bl_label = "Apply Custom Shapes"
    bl_idname = ".".join((config.id_name, "custom_shapes"))

    def execute(self, context):
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            self.report({"ERROR"},"The active object is not an armature.")
            return {'CANCELLED'}
        # shapes = import_shape_collection(config.custom_shapes_filename)
        rm_armature = RM_Armature(armature=armature)

        Unused(armature=rm_armature).hide()

        Head(armature=rm_armature).setup()
        Neck(armature=rm_armature).setup()

        TwistBones(armature=rm_armature).setup()
        Arms(armature=rm_armature).setup()
        Hands(armature=rm_armature).setup()
        Shoulders(armature=rm_armature).setup()
        Spine(armature=rm_armature).setup()
        Boobs(armature=rm_armature).setup()

        Waist(armature=rm_armature).setup()
        Legs(armature=rm_armature).setup()
        Tail(armature=rm_armature).setup()

        try:
            rm_armature.get_bone("n_throw").set_visibility(visible=False)

        except Exception as e:
            self.report({"ERROR"}, str(e))
            return {'CANCELLED'}

        return {'FINISHED'}