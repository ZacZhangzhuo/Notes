import mola
import random
import Rhino.Geometry as rg

mMesh = mola.construct_single_face(
    [mola.Vertex(0, 0, 0), mola.Vertex(10, 0, 0), mola.Vertex(10, 10, 0), mola.Vertex(0, 10, 0)]
)

newMesh = mola.Mesh()

for face in mMesh.faces:
    newFaces = mola.subdivide_face_extrude_to_point_center(face, 0)
    newMesh.faces.extend(newFaces)

mMesh = newMesh
mMesh.update_topology()
mMesh = mola.subdivide_mesh_catmull(mMesh)

newMesh = mola.Mesh()
for face in mMesh.faces:
    newFaces = mola.subdivide_face_split_grid(face, 2, 1)
    newMesh.faces.extend(newFaces)

mMesh = newMesh


for face in mMesh.faces:
    face.group = "plot"

newMesh = mola.Mesh()
for f in mMesh.faces:
    if f.group == "plot":
        new_faces = mola.subdivide_face_extrude_tapered(f, 0, 0.3, True)
        for nf in new_faces[:-1]:
            nf.group = "circulation"
            nf.color = (1, 0, 0)
        # [-1] is take the last element [:-1] is for taking all elements
        new_faces[-1].group = "construction"
        new_faces[-1].color = (0.5, 0, 1)
        newMesh.faces.extend(new_faces)
    else:
        newMesh.faces.append(f)


mMesh = newMesh

########################################################################

newMesh = mola.Mesh()
for face in mMesh.faces:
    if face.group == "construction":
        if random.random() < 0.2:
            newFaces = mola.subdivide_face_extrude_to_point_center(face, 1)
            for newFace in newFaces:
                newFace.group = "park"
                newFace.color = (0, 1, 0)
            newMesh.faces.extend(newFaces)
        else:
            floorNumber = random.randint(5, 20)
            buildingSurface = [face]
            for i in range(floorNumber):
                buildingSurface.extend(mola.subdivide_face_extrude(buildingSurface[-1], 0.1, False))
                buildingSurface.pop(-6)
            for newFace in buildingSurface:
                newFace.group = "building"
                newFace.color = (0, 0, 1)
            newMesh.faces.extend(buildingSurface)

    newMesh.faces.append(face)

newMesh.update_topology()
newMesh = mola.subdivide_mesh_catmull(newMesh)
newMesh = mola.subdivide_mesh_catmull(newMesh)

mMesh = newMesh

Mesh = mola.module_rhino.display_mesh(mMesh)
