# IMPORT
from copy import copy
import Rhino.Geometry as rg
import math
from ghpythonlib.components import ColourRGB

# INPUTS
# NautilusSize
# PiceSize
# PiceNumber
# Sharpness
# CircleSize
# CircleRotation
SketchLines1Extend = 100

# CLASS
class Nautilus(object):
    # initialize
    def __init__(self, NautilusSize, PiceSize, PiceNumber, Sharpness, CircleSize, CircleRotation):
        self.nautilusSize = NautilusSize
        self.piceSize = PiceSize
        self.piceNumber = PiceNumber
        self.sharpness = Sharpness
        self.circle = CircleSize
        self.circleRotation = CircleRotation
        self.Sketch = Sketch()
        self.SketchLines1 = []
        self.SketchLines2 = []
        self.SketchLines3 = []
        self.SketchLines4 = []
        self.SketchLines5 = []
        self.circles = self.__MakeSpiralCircles(
            self.__MakeSpiralPoints(NautilusSize, PiceSize, PiceNumber, Sharpness), CircleSize
        )
        self.objects = self.__makeObjects()
        self.colours = self.__makeColours()

    def __FibonacciSharpness(PiceNumber, Sharpness):
        zSharpness = []
        zSharpness.append(Sharpness)
        zSharpness.append(Sharpness)
        for i in range(PiceNumber - 2):
            zSharpness.append(zSharpness[i] + zSharpness[i + 1])
        return zSharpness

    def __RotateCircle(self, circle, rotation):
        # circle = rg.Circle(x)
        circle.Transform(
            rg.Transform.Rotation(
                rg.Vector3d(1, 0, 0),
                rg.Vector3d(math.cos(rotation), math.sin(rotation), 0),
                circle.Center,
            )
        )
        return circle

    def __MakeSpiralPoints(self, NautilusSize, PiceSize, PiceNumber, Sharpness):
        # Outcome point3d[]
        points = []
        sketchPoints = []

        for t in range(PiceNumber + SketchLines1Extend):
            r = NautilusSize * t
            x = r * math.cos(2 * math.pi * t * PiceSize * 0.1)
            y = r * math.sin(2 * math.pi * t * PiceSize * 0.1)
            #  ys = FibonacciSharpness(PiceNumber, Sharpness)#! FibonacciSharpness
            #  points.append(rg.Point3d(x,y,ys[t]))#! FibonacciSharpness
            #  print ys
            if t < PiceNumber:
                points.append(rg.Point3d(x, y, Sharpness * t * t))
            sketchPoints.append(rg.Point3d(x, y, Sharpness * t * t))

        # * Sketch
        self.SketchLines1 = self.Sketch.PointsToCurve(sketchPoints)

        return points

    def __MakeSpiralCircles(self, SpiralPoints, Size):
        circles = []
        for i in range(len(SpiralPoints) - 1):
            # Make the vector
            vector = rg.Vector3d(SpiralPoints[i + 1] - SpiralPoints[i])
            # Make the plane
            plane = rg.Plane((SpiralPoints[i + 1] + SpiralPoints[i]) / 2, vector)

            # Rotate plane #!Hard part
            xAxis = copy(plane.XAxis)
            xAxis.Transform(rg.Transform.ProjectAlong(rg.Plane.WorldXY, plane.YAxis))
            plane.Transform(rg.Transform.Rotation(plane.XAxis, xAxis, plane.Origin))
            if plane.YAxis.Z < 0:
                plane = rg.Plane(plane.Origin, -plane.XAxis, -plane.YAxis)

            # Make circle
            circle = rg.Circle(plane, Size * (i + 1))
            circles.append(
                self.__RotateCircle(circle, (i / (len(SpiralPoints) - 1)) * CircleRotation)
            )

        return circles

    def __makeColours(self):
        Colours = []
        for i in range(len(self.circles) - 1):
            colour = ColourRGB(
                255,
                i * 255 / (len(self.circles) - 1),
                i * 255 / (len(self.circles) - 1),
                i * 255 / (len(self.circles) - 1),
            )
            Colours.append(colour)
        return Colours

    def __makeObjects(self):
        Nautilus = []
        for i in range(len(self.circles) - 1):
            Nautilus.append(
                rg.NurbsSurface.CreateRuledSurface(
                    self.circles[i].ToNurbsCurve(), self.circles[i + 1].ToNurbsCurve()
                )
            )
        return Nautilus


class Sketch(object):
    def PointsToCurve(self, points):
        return rg.NurbsCurve.Create(False, 2, points)


nautilus = Nautilus(NautilusSize, PiceSize, PiceNumber, Sharpness, CircleSize, CircleRotation)
Objects = nautilus.objects
Colours = nautilus.colours
Circles = nautilus.circles
SketchLines1 = nautilus.SketchLines1
SketchLines2 = nautilus.SketchLines2
SketchLines3 = nautilus.SketchLines3
SketchLines4 = nautilus.SketchLines4
