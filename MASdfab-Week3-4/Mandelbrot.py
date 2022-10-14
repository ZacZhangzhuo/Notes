import math
import Rhino.Geometry as rg
import mola

DIM = 16
scale = 100
mandelbrot = []
maxIteration = 10
n = 8


class zVector:
    """A vector object constructed by X, Y and Z"""

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z


def Remap(number, min0, max0, min1, max1):
    """Map a number from domain (min0, max0) into (min1, max1)"""
    return (number - min0) / (max0 - min0) * (max1 - min1) + min1


class Spherical(object):
    def __init__(self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi


def spherical(x, y, z):
    r = math.sqrt(x * x + y * y + z * z)
    theta = math.atan2(math.sqrt(x * x + y * y), z)
    phi = math.atan2(y, x)
    return Spherical(r, theta, phi)


for i in range(DIM):
    for j in range(DIM):
        edge = False
        for k in range(DIM):

            x = Remap(i, 0, DIM, -1, 1)
            y = Remap(j, 0, DIM, -1, 1)
            z = Remap(k, 0, DIM, -1, 1)

            zeta = zVector(0, 0, 0)
            iteration = 0

            while True:

                sphericalZ = spherical(zeta.X, zeta.Y, zeta.Z)
                newx = (
                    math.pow(sphericalZ.r, n)
                    * math.sin(sphericalZ.theta * n)
                    * math.cos(sphericalZ.phi * n)
                )
                newy = (
                    math.pow(sphericalZ.r, n)
                    * math.sin(sphericalZ.theta * n)
                    * math.sin(sphericalZ.phi * n)
                )
                newz = math.pow(sphericalZ.r, n) * math.cos(sphericalZ.theta * n)

                zeta.X = newx + x
                zeta.Y = newy + y
                zeta.Z = newz + z

                iteration = iteration + 1

                if sphericalZ.r > 16:
                    if edge:
                        edge = False
                    break
                
                
                if iteration > maxIteration:
                    if ~edge:
                        edge = True
                        mandelbrot.append(zVector(100 * x, 100 * y, 100 * z))
                    break

pts = []
for vec in mandelbrot:
    pts.append(rg.Point3d(vec.X, vec.Y, vec.Z))

outTemp = pts
