import mola
import math
import Rhino.Geometry as rg

molaMesh = mola.construct_sphere(radius=5, u_res=8, v_res=8)

for v in molaMesh.vertices:
    if v.z > 0:
        v.z *= 1.8

molaMesh = mola.subdivide_mesh_catmull(molaMesh)

for f in molaMesh.faces:
    molaMesh.faces.extend(mola.subdivide_face_extrude_tapered(f, 10,0.5, True))
    
    
Mesh = mola.module_rhino.display_mesh(molaMesh)

# outTemp = []
# for face in molaMesh.faces:
    # outTemp.append(rg.Point3d(mola.face_center(face).x, mola.face_center(face).y, mola.face_center(face).z))
