import mola
import math
from mola import module_rhino
from ghpythonlib import treehelpers
import random

# dim = int(math.floor(len(Values) ** (1 / 3) + 0.0001))


# # ! Too tree
# facesArray = []
# lineArray = []
# for i in range(dim):
#     facesArray.append(Values[dim*dim * i : dim*dim * (i + 1)])

# for face in facesArray:
#     tempArray = []
#     for i in range(dim):
#         tempArray.append(face[dim * i : dim * (i + 1)])
#     lineArray.append(tempArray)
# # ! End to tree

# for i in range(dim):
#     for j in range(dim):
#         for k in range(dim):
#             lineArray[0][j][k]=0
#             lineArray[-1][j][k] =0
#             lineArray[i][0][k]=0
#             lineArray[i][-1][k] =0
#             lineArray[i][j][0]=0
#             lineArray[i][j][-1] =0


# # ! Play around with
# newArray = []
# # for i in range(dim):
# #     for j in range(dim):
# #         for k in range(dim):


# # ! Too list
# values = []
# for i in range(dim):
#     for j in range(dim):
#         for k in range(dim):
#             values.append(newArray[i][j][k] )
# # x = treehelpers.list_to_tree(lineArray)

# # print (len(values))
# cubes = mola.mesh_marching_cubes(dim, dim, dim, values, 0.5)
# cubes.update_topology()
# mola.color_faces_by_vertical_angle(cubes.faces)

# outTemp = module_rhino.display_mesh(cubes)


dim = 50


values = []
for i in range(dim):
    for j in range(dim):
        ratio = random.randint(0, i)/dim*0.2
        for k in range(dim):
            if k < dim * ratio:
                values.append(1)
            else:
                values.append(0)
cubes = mola.mesh_marching_cubes(dim, dim, dim, values, 0.5)

cubes.update_topology()
# mola.color_faces_by_vertical_angle(cubes.faces)

outTemp = module_rhino.display_mesh(cubes)
