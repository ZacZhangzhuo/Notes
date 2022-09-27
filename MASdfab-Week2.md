# MAS dfab - Week 2

---

## Enumeration

```Python
    for i, rectangle in enumerate(geo): #!
        r = deepcopy(rectangle)
        degree = math.radians(random.randint(-rectangle, Corner(2).Y))

        # The for loop is the same as below

    for i in range(len(geo)):  #!
        r = deepcopy(rectangle)
        degree = math.radians(random.randint(-rectangle, Corner(2).Y))
```

## Interval

- Represents an interval in one-dimensional space, that is defined as two extrema or bounds.
- https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Interval.htm

## Read images

```Python
    import System
    import os

    HERE = ghenv.LocalScope.ghdoc.Path
    dir_path = os.path.dirname(HERE)
    bitmap = System.Drawing.Image.FromFile(dir_path + "\\" + inTemp + ".png")

    deltaPixelX = bitmap.Width / nx
    deltaPixelT = bitmap.Height / ny

    # Ask the colour of the pixie
    color = System.Drawing.Bitmap.GetPixel(bitmap, x, y)
```
