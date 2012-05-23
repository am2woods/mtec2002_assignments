import blender
import bpy
import math
import mathutils

class Makelowerhalf(bpy.types.Operator) :
    bl_idname = "mesh.make_3DS_lower_half"
    bl_label = "Add 3DS_lower_half"
	
		def invoke(self, context, event) :
			Vertices = \
				[
					mathutils.Vector((0, 0, 0)),
					mathutils.Vector((4, 0, 0)),
					mathutils.Vector((0, 3, 0)),
					mathutils.Vector((4, 3, 0)),
					mathutils.Vector((0, 0, 2)),
					mathutils.Vector((4, 0, 2)),
					mathutils.Vector((0, 3, 2)),
					mathutils.Vector((4, 3, 2)),
				[
				
			NewMesh = bpy.data.meshes.new("3DS_lower_half")
			
			"""NewMesh.from_pydata \
				(
					Vertices,
					[],
				)"""
			NewMesh.update()
			NewObj = bpy.data.objects.new("3DS_lower_half", NewMesh)
			context.scene.objects.link(NewObj)
			return {"FINISHED"}
bpy.utils.register_class(Makelowerhalf)
			
class Makehinge(bpy.types.Operator) :
    bl_idname = "mesh.make_3DS_hinge"
    bl_label = "Add 3DS_hinge"
	
		def invoke(self, context, event) :
			Vertices = \
				[
					mathutils.Vector((0, 0, 0)),
					mathutils.Vector((4, 0, 0)),
					mathutils.Vector((0, 1, 0)),
					mathutils.Vector((4, 1, 0)),
					mathutils.Vector((0, 0, 1)),
					mathutils.Vector((4, 0, 1)),
					mathutils.Vector((0, 1, 1)),
					mathutils.Vector((4, 1, 1)),
				[
				
			NewMesh = bpy.data.meshes.new("3DS_hinge")
			
			"""NewMesh.from_pydata \
				(
					Vertices,
					[],
				)"""
			NewMesh.update()
			NewObj = bpy.data.objects.new("3DS_hinge", NewMesh)
			context.scene.objects.link(NewObj)
			return {"FINISHED"}
bpy.utils.register_class(Makehinge)

class Makeupperhalf(bpy.types.Operator) :
    bl_idname = "mesh.make_3DS_upper_half"
    bl_label = "Add 3DS_upper_half"
	
		def invoke(self, context, event) :
			Vertices = \
				[
					mathutils.Vector((0, 0, 0)),
					mathutils.Vector((3.5, 0, 0)),
					mathutils.Vector((0, 2.6, 0)),
					mathutils.Vector((3.5, 2.6, 0)),
					mathutils.Vector((0, 0, 1)),
					mathutils.Vector((3.5, 0, 1)),
					mathutils.Vector((0, 2.6, 1)),
					mathutils.Vector((3.5, 2.6, 1)),
				[
				
			NewMesh = bpy.data.meshes.new("3DS_upper_half")
			
			"""NewMesh.from_pydata \
				(
					Vertices,
					[],
				)"""
			NewMesh.update()
			NewObj = bpy.data.objects.new("3DS_upper_half", NewMesh)
			context.scene.objects.link(NewObj)
			return {"FINISHED"}
bpy.utils.register_class(Makeupperhalf)			