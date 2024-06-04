import bpy, mathutils, math, os
from ..utils import LegacyBoner
from ..utils import bones;

class TestOperator(bpy.types.Operator):
    bl_label = "Test Button"
    bl_idname = "xivbc.test"
    
    def execute(self, context):
        file_path = directory=os.path.join('assets', 'BoneCleaner-CustomShapes.blend') + r'\Collection'
        bpy.ops.wm.append(directory=file_path, filename='CustomShapes', link=False)
        return {'FINISHED'}