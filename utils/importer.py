import os
import bpy


def importShapeCollection(self) -> dict:
        imported_shapes: dict = {}

        script_file = os.path.realpath(__file__)
        script_dir = os.path.dirname(script_file)
        addon_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
        
        assets_dir = "assets"
        blendfile = "BoneCleaner-CustomShapes.blend"
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