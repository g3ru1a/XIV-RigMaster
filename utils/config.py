class Config:
    def __init__(self, name, id_name, author, version, blender, location, description, warning, doc_url, category, custom_shapes_filename):
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
        self.custom_shapes_filename = custom_shapes_filename

config = Config(
    name="XIV RigMaster",
    id_name="xivrm",
    author="G3ru1a",
    version=(0, 3),
    blender=(4, 0, 0),
    location="View3D > UI > XIV RigMaster",
    description="XIV RigMaster enhances Final Fantasy XIV character models by streamlining armatures with custom shapes and adding functionality such as IK and Bone Constraints, ensuring a cleaner and more professional rigging process. Perfect for animators and modellers looking to elevate their creations.",
    warning="",
    doc_url="",
    category="XIV RigMaster 0.3",
    custom_shapes_filename="RigMaster-CustomShapes-Dawntrail.blend"
)
