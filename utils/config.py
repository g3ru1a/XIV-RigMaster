class Config:
    def __init__(self, name, id_name, author, version, blender, location, description, warning, doc_url, category):
        self.name = name
        self.id_name = id_name
        self.author = author
        self.version = version
        self.blender = blender
        self.location = location
        self.description = description
        self.warning = warning
        self.doc_url = doc_url
        self.category = category

config = Config(
    name="XIV Bone Cleaner",
    id_name="xivbc",
    author="G3ru1a",
    version=(0, 3),
    blender=(4, 0, 0),
    location="View3D > UI > XIV Bone Cleaner",
    description="Cleans up the bones from a Meddle Exported .gltf Model",
    warning="",
    doc_url="",
    category="XIV Bone Cleaner 0.3"
)

# Example usage
print(config.name)  # Output: XIV Bone Cleaner
