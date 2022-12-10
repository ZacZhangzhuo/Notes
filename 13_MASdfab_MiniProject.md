# MAS dfab - Mini Project



## New orientation function

```Python
def OrientPlane(plane):
    zAxis = plane.ZAxis
    if zAxis.Z < 0: zAxis = -zAxis
    outPlane = rg.Plane(plane.Origin, zAxis)
    xAxis = copy.copy(outPlane.XAxis)
    xAxis.Transform(rg.Transform.ProjectAlong(rg.Plane.WorldXY, outPlane.YAxis))
    outPlane.Transform(rg.Transform.Rotation(outPlane.XAxis, xAxis, outPlane.Origin))
    if outPlane.YAxis.Z <0 : outPlane = rg.Plane(outPlane.Origin, -outPlane.XAxis, -outPlane.YAxis)
    return outPlane
```

## An interesting Q&A

![](13_MASdfab_MiniProject/13_MASdfab_MiniProject_2022-12-07-09-54-22.png)