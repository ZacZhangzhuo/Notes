import mola
import math
from mola import module_rhino

dim = int(math.floor(len(Values) ** (1 / 3) + 0.0001))

for i in range(len(Values)): 
    if (i <= dim*dim or i >= dim*dim*(dim-1) ) : Values[i] = 0
    if ( i % dim == 0 or i % dim == dim-1): Values[i] = 0
    # if ( i  % (dim*dim) == 0 or i % (dim*dim) == dim-1): Values[i] = 0


print(dim)


# Give bounds to the ball

cubes = mola.mesh_marching_cubes(dim, dim, dim, Values, 0.5)
cubes.update_topology()
mola.color_faces_by_vertical_angle(cubes.faces)

outTemp = module_rhino.display_mesh(cubes)
