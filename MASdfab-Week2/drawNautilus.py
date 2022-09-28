# IMPORT
from copy import copy
import Rhino.Geometry as rg
import math
from ghpythonlib.components import ColourRGB
import sys

# INPUTS
# NautilusSize
# PiceSize
# PiceNumber
# Sharpness
# CircleSize
# CircleRotation
SketchParam1 = 80
SketchParam2 = 50
SketchParam3 = 80

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
        self.SketchPoints = []
        self.SketchLines1 = []
        self.SketchLines2 = []
        self.SketchLines3 = []
        self.SketchLines4 = []
        self.SketchLines5 = []
        self.circles = self.__MakeSpiralCircles(
            self.__MakeSpiralPoints(NautilusSize, PiceSize, PiceNumber, Sharpness),
            CircleSize,
            self.SketchPoints,
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

    def __Rotate(self, circle, rotation):
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

        for t in range(PiceNumber + SketchParam1):
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
        if IsSketch:
            self.SketchLines1 = self.Sketch.PointsToCurve(sketchPoints)
        self.SketchPoints = sketchPoints

        return points

    def __MakeSpiralCircles(self, SpiralPoints, Size, SketchPoints):
        circles = []
        sketchCircles = []
        for i in range(len(SketchPoints) - SketchParam2 - 1):
            # Make the vector
            vector = rg.Vector3d(SketchPoints[i + 1] - SketchPoints[i])
            # Make the plane
            plane = rg.Plane((SketchPoints[i + 1] + SketchPoints[i]) / 2, vector)

            # Rotate plane #!Hard part
            xAxis = copy(plane.XAxis)
            xAxis.Transform(rg.Transform.ProjectAlong(rg.Plane.WorldXY, plane.YAxis))
            plane.Transform(rg.Transform.Rotation(plane.XAxis, xAxis, plane.Origin))
            if plane.YAxis.Z < 0:
                plane = rg.Plane(plane.Origin, -plane.XAxis, -plane.YAxis)

            # Make circle
            circle = rg.Circle(plane, Size * (i + 1))
            if i < len(SpiralPoints) - 1:
                circles.append(
                    self.__Rotate(circle, (i / (len(SpiralPoints) - 1)) * CircleRotation)
                )
            else:
                # * Sketch
                if IsSketch:
                    self.SketchLines2.append(circle)
            if IsSketch:
                if i < len(SketchPoints) - 1 - SketchParam3 and i % 2 == 0:
                    # print i
                    # print (len(SketchPoints) - 1- SketchParam3)
                    # rg.ArcCurve()
                    sketchCircles.append(
                        self.__Rotate(
                            rg.Rectangle3d(
                                plane,
                                rg.Interval(-Size * (i + 1), Size * (i + 1)),
                                rg.Interval(-Size * (i + 1), Size * (i + 1)),
                            ),
                            i / (len(SketchPoints) - 1) * CircleRotation,
                        ).ToPolyline()
                    )

        # * Sketch - extend rectangles
        # for rectangles in sketchCircles:
        line1 = rg.ArcCurve()
        # line1.ClosestPoint()

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


rg.Point3d()