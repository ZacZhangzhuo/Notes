import mola


m = mola.construct_icosahedron(Radius)

faces = []
for face in m.faces:
    face = mola.subdivide_face_split_grid(face, Temp, Temp)
    faces.append(face)

# m.faces = faces
# mola.color_faces_by_vertical_angle(m.faces)

Mesh = mola.module_rhino.display_mesh(m)
# torus = mola.construct_torus(Radius, Radius2)


# Mesh = mola.module_rhino.display_mesh(torus)
