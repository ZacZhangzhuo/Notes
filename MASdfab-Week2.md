# MAS dfab - Week 2

---

## 1. <a name='Enumeration'></a>Enumeration

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
* Represents an interval in one-dimensional space, that is defined as two extrema or bounds.
* https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Interval.htm
