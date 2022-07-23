import bpy
import os

from bpy.types import Operator, Panel
from bpy.props import StringProperty, IntProperty, BoolProperty


bl_info = {
    "name": "Export to Godot",
    "version": (0, 0, 1),
    "blender": (3, 2, 0),
    "location": "File > Import-Export",
    "category": "Import-Export",
}


class ExportToGodotPanel(Panel):
    bl_idname = "export.godot.panel"
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    bl_context = "objectmode"
    bl_label = "Export To Godot"

    def draw(self, context) :
        layout = self.layout

        box = layout.box();
        box.prop(context.scene, "export_to_godot_path")
        box.operator("export.godot", text = "Export")


class ExportToGodot(Operator):
    """Export To Godot"""
    bl_idname = "export.godot"
    bl_label = "Export to Godot"
    bl_options = {'REGISTER'}

    def execute(self, context):

        my_path = os.path.abspath(context.scene.export_to_godot_path)

        if my_path.endswith("/"):
            my_path = my_path.removesuffix("/")

        # get list of selected objects
        selected_list = context.selected_objects

        # loop all initial selected objects
        for o in selected_list:
            # deselect all in scene
            bpy.ops.object.select_all(action='DESELECT')

            obj = context.scene.objects[o.name]
            objType = getattr(obj, 'type', '')

            if objType != 'MESH':
                continue

            # select the object
            obj.select_set(True)

            # create directory
            outpath = os.path.join(my_path, o.name)
            if not os.path.isdir(outpath):
                os.mkdir(outpath)

            # set filename
            outpath = os.path.join(outpath, o.name + '.glb')

            # export it
            # many other parameters can be added here

            bpy.ops.export_scene.gltf(
                filepath=outpath,
                check_existing=False,
                use_selection=True,
                export_apply=True
            )
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ExportToGodot.bl_idname)


def register():
    bpy.utils.register_class(ExportToGodot)
    bpy.utils.register_class(ExportToGodotPanel)
    # bpy.types.TOPBAR_MT_file_export.append(menu_func)
    bpy.types.Scene.export_to_godot_path = StringProperty(name="Path", default=".", subtype="DIR_PATH",description="Path to the Godot Assets")


def unregister():
    bpy.utils.unregister_class(ExportToGodotPanel)
    bpy.utils.unregister_class(ExportToGodot)
    # bpy.types.TOPBAR_MT_file_export.remove(menu_func)
    del bpy.types.Scene.export_to_godot_path



