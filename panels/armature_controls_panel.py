from ..utils.config import data as config
import bpy, mathutils, math

class VisibilityProperties(bpy.types.PropertyGroup):
    clothing_visible: bpy.props.BoolProperty(name="Clothing Visible", default=True) # type: ignore
    gear_visible: bpy.props.BoolProperty(name="Gear Visible", default=True) # type: ignore
    twists_visible: bpy.props.BoolProperty(name="Twists Visible", default=True) # type: ignore
    tail_visible: bpy.props.BoolProperty(name="Tail Visible", default=True) # type: ignore
    left_hand_visible: bpy.props.BoolProperty(name="Left Hand Visible", default=True) # type: ignore
    right_hand_visible: bpy.props.BoolProperty(name="Right Hand Visible", default=True) # type: ignore
    left_arm_visible: bpy.props.BoolProperty(name="Left Arm Visible", default=True) # type: ignore
    right_arm_visible: bpy.props.BoolProperty(name="Right Arm Visible", default=True) # type: ignore
    left_leg_visible: bpy.props.BoolProperty(name="Left Leg Visible", default=True) # type: ignore
    right_leg_visible: bpy.props.BoolProperty(name="Right Leg Visible", default=True) # type: ignore

    show_extra: bpy.props.BoolProperty(name="Show Extra", default=False) # type: ignore

class VIEW3D_PT_ControlsPanel(bpy.types.Panel):
    bl_label = "Armature Controls"
    bl_idname = "VIEW3D_PT_ControlsPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = config["category"]
    
    def draw(self, context):
        layout = self.layout
        props: VisibilityProperties = context.scene.visibility_props

        row = layout.row()
        row.operator(".".join((config["id_name"], "toggle_clothing")), depress=props.clothing_visible)
        row.operator(".".join((config["id_name"], "toggle_gear")), depress=props.gear_visible)
        
        row = layout.row()
        arm_depress = True if props.left_arm_visible == props.right_arm_visible == True else False
        hands_depress = True if props.left_hand_visible == props.right_hand_visible == True else False
        row.operator(".".join((config["id_name"], "toggle_arms")), depress=arm_depress)
        row.operator(".".join((config["id_name"], "toggle_hands")), depress=hands_depress)
        
        row = layout.row()
        leg_depress = True if props.left_leg_visible == props.right_leg_visible == True else False
        row.operator(".".join((config["id_name"], "toggle_legs")), depress=leg_depress)
        row.operator(".".join((config["id_name"], "toggle_twists")), depress=props.twists_visible)

        row = layout.row()
        row.operator(".".join((config["id_name"], "toggle_tail")), depress=props.tail_visible)

        # Create a collapsible box
        box = layout.box()
        row = box.row()
        row.prop(props, "show_extra", icon="TRIA_DOWN" if props.show_extra else "TRIA_RIGHT", icon_only=True, emboss=False)
        row.label(text="Extra")

        
        # Display buttons conditionally
        if props.show_extra:
            box_row = box.row()
            box_row.operator(".".join((config["id_name"], "toggle_left_hand")), depress=props.left_hand_visible)
            box_row.operator(".".join((config["id_name"], "toggle_right_hand")), depress=props.right_hand_visible)

            box_row = box.row()
            box_row.operator(".".join((config["id_name"], "toggle_left_arm")), depress=props.left_arm_visible)
            box_row.operator(".".join((config["id_name"], "toggle_right_arm")), depress=props.right_arm_visible)

            box_row = box.row()
            box_row.operator(".".join((config["id_name"], "toggle_left_leg")), depress=props.left_leg_visible)
            box_row.operator(".".join((config["id_name"], "toggle_right_leg")), depress=props.right_leg_visible)


    
