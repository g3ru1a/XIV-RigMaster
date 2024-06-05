from contextlib import contextmanager
import os
import sys
import bpy, importlib
from pathlib import Path

@contextmanager
def mode_set(mode="POSE"):
    prev_mode = bpy.context.object.mode
    bpy.ops.object.mode_set(mode=mode)
    try:
        yield
    finally:
        bpy.ops.object.mode_set(mode=prev_mode)

def import_shape_collection(filename = "BoneCleaner-CustomShapes.blend") -> dict:
        imported_shapes: dict = {}

        addon_dir = get_addon_absolute_path()
        
        assets_dir = "assets"
        blendfile = filename
        category = "Collection"
        collection_name = "CustomShapes"

        # Get Collection
        imported_collection: bpy.types.Collection = bpy.data.collections.get(collection_name)

        # If the collection doesn't exist, import Collection from Assets File
        if not imported_collection:
            bpy.ops.wm.append(
                filepath=os.path.join(addon_dir, assets_dir, blendfile, category, collection_name),
                filename=collection_name,
                directory=os.path.join(addon_dir, assets_dir, blendfile, category),
                link=False)
            imported_collection = bpy.data.collections.get(collection_name)

        # Load each shape
        if imported_collection:
            # Retrieve all objects in the imported collection
            imported_shapes = {obj.name: obj for obj in imported_collection.objects}
            imported_collection.hide_render = True
            imported_collection.hide_viewport = True
            return imported_shapes
        else:
            raise ValueError(f"Collection '{collection_name}' was not found in the file.")
        
def get_addon_absolute_path() -> str:
    script_file = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_file)
    addon_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    return addon_dir

def all_operators_in_module(operators_module: any, register: bool = True) -> None:
    for name in dir(operators_module):
        obj = getattr(operators_module, name)
        if isinstance(obj, type) and issubclass(obj, bpy.types.Operator):
            if register: 
                bpy.utils.register_class(obj)
                print(f"Registered: {obj}")
            else:
                bpy.utils.unregister_class(obj)
                print(f"Unregistered: {obj}")

def lists_are_equal(a: list, b: list) -> bool:
    return a == b