# MAS dfab - Week 2

---

Contents
<!-- vscode-markdown-toc -->
* 1. [Enumeration](#Enumeration)
* 2. [Interval](#Interval)
* 3. [Read images](#Readimages)
* 4. [Remap function](#Remapfunction)
* 5. [Ask the colour of the pixie](#Askthecolourofthepixie)
* 6. [Mesh Colour (Colour is stored in the vertex data)](#MeshColourColourisstoredinthevertexdata)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='Enumeration'></a>Enumeration

```Python
    for i, rectangle in enumerate(geo): #!
        r = deepcopy(rectangle)
        degree = math.radians(random.randint(-rectangle, Corner(2).Y))

        # The for loop is the same as below

    for i in range(len(geo)):  #!
        r = deepcopy(rectangle)
        degree = math.radians(random.randint(-rectangle, Corner(2).Y))
```

##  2. <a name='Interval'></a>Interval

- Represents an interval in one-dimensional space, that is defined as two extrema or bounds.
- https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Interval.htm

##  3. <a name='Readimages'></a>Read images

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

##  4. <a name='Remapfunction'></a>Remap function

```Python
    def remap(value, low1, high1, low2, high2):
        new_value = low2 + (value-low1)*(high2-low2)/(high1-low1)
        return new_value
```

##  5. <a name='Askthecolourofthepixie'></a>Ask the colour of the pixie

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

##  6. <a name='MeshColourColourisstoredinthevertexdata'></a>Mesh Colour (Colour is stored in the vertex data)

```Python
    box_mesh.VertexColors.CreateMonotoneMesh(self.color)
```

## One reason why AutoCompletion does not work on my PC

* Some other paths occupied the AutoCompletion but cannot do that well. So we have to clear every extra path, and don't let the useless things exist.

```Json
      "python.autoComplete.extraPaths": [
  
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\scripts",
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
    "C:\\Applications\\Rhino 7\\Plug-ins\\IronPython\\Lib",
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
    // There is a "C:\Program Files\Common Files\McNeel\Rhinoceros\7.0\Plug-ins\CodeListener" very annoying and occupied the autoCompletion when scripting GHPython. Delete this one then autoCompletion is fine.
    "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib\\ghpythonlib"
  ],
```