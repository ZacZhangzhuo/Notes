import mola
from mola import module_rhino
import Rhino.Geometry as rg
import Rhino.Geometry.Intersect as intersection
import zorse
import csv
import math


def Distance(vertex1, vertex2):
    return math.pow(
        math.pow(vertex1.x - vertex2.x, 2)
        + math.pow(vertex1.y - vertex2.y, 2)
        + math.pow(vertex1.z - vertex2.z, 2),
        0.5,
    )


def DecreaseAbs(Number1, Decrease):
    if Number1 < 0:
        Number1 = Number1 + Decrease
    else:
        Number1 = Number1 - Decrease
    return Number1


DIM32 = r"C:\Zac\19 Github\Notes\MASdfab-Week5\DIM32.csv"
DIM64 = r"C:\Zac\19 Github\Notes\MASdfab-Week5\DIM64.csv"
DIM128 = r"C:\Zac\19 Github\Notes\MASdfab-Week5\DIM128.csv"

data = []
with open(DIM32) as f:
    reader = csv.reader(f)
    # headers = next(reader)
    # print(headers)
    for row in reader:
        data.extend(row)


dim = int(math.floor(len(data) ** (1 / 3) + 0.0001))


# ! Too tree
facesArray = []
lineArray = []
for i in range(dim):
    facesArray.append(data[dim * dim * i : dim * dim * (i + 1)])

for face in facesArray:
    tempArray = []
    for i in range(dim):
        tempArray.append(face[dim * i : dim * (i + 1)])
    lineArray.append(tempArray)
# ! End to tree

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            lineArray[0][j][k] = 0
            lineArray[-1][j][k] = 0
            lineArray[i][0][k] = 0
            lineArray[i][-1][k] = 0
            lineArray[i][j][0] = 0
            lineArray[i][j][-1] = 0


# ! Too list
values = []
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            values.append(int(lineArray[i][j][k]))

cubes = mola.mesh_marching_cubes(dim, dim, dim, values, 0.5)

# Marching cubes mesh to the center
for vertex in cubes.vertices:
    vertex.x = vertex.x - dim / 2
    vertex.y = vertex.y - dim / 2
    vertex.z = vertex.z - dim / 2


# Get the minimal distance
Center = mola.Vertex(0, 0, 0)
distance = Distance(Center, cubes.vertices[0])
for vertex in cubes.vertices:
    if Distance(Center, vertex) <= distance:
        distance = Distance(Center, vertex)


for vertex in cubes.vertices:
    ray = rg.Ray3d(rg.Point3d(0, 0, 0), rg.Vector3d(vertex.x, vertex.y, vertex.z))
    intersectionPoint = intersection.Intersection.MeshRay(inTemp, ray)

    intersectionPoint = ray.PointAt(intersectionPoint)  # type: ignore
    vertex.x = intersectionPoint.X + vertex.x*0.1
    vertex.y = intersectionPoint.Y  + vertex.y*0.1
    vertex.z = intersectionPoint.Z  +vertex.z*0.1
    
print (DecreaseAbs(10, 10))

cubes.update_topology()
mola.color_faces_by_vertical_angle(cubes.faces)

outTemp = module_rhino.display_mesh(cubes)
