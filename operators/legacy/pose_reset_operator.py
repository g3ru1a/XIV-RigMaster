import bpy
from ...utils import LegacyBoner
from ...utils.config import config
from ...utils import bones;

class ARMATURE_OT_PoseReset(bpy.types.Operator):
    bl_label = "Reset Pose"
    bl_idname = ".".join((config.id_name, "pose_reset"))
    
    def execute(self, context):
        # Check if an Armature is selected
        # Get the armature object
        armature: bpy.types.Object = bpy.context.active_object
        if not armature or armature.type != 'ARMATURE':
            print("The active object is not an armature.")
            return
        
        # Remove Animation Data
        armature.animation_data_clear();

        current_mode = bpy.context.object.mode
        # Reset Bone Positions and Rotations
        bpy.ops.object.mode_set(mode='POSE')
        for bone in armature.pose.bones:
            # Clear transformations
            bone.location = (0, 0, 0)      # Reset translation
            bone.rotation_quaternion = (1, 0, 0, 0)  # Reset quaternion rotation
            bone.rotation_euler = (0, 0, 0)  # Reset Euler rotation (will only work for objects using this mode)
        bpy.ops.object.mode_set(mode=current_mode)

        # Fix Arm Bone Length
        LegacyBoner.EditBone.tail2head(armature, bones.elbow_left, bones.wrist_left)
        LegacyBoner.EditBone.tail2head(armature, bones.elbow_right, bones.wrist_right)

        # Make sure Armature is showed in front
        armature.show_in_front = True
        return {'FINISHED'}