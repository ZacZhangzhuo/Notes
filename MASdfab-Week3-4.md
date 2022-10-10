# MAS dfab - Week 3-4 - Robotic Dancing, Robotic Drawing, Generative City



## L-System

```Python
    import Rhino.Geometry as rg
    import math


    rule1_predecessor = "X"
    rule1_successor = "F+[[X]-X]-F[-FX]+X"
    rule2_predecessor = "F"
    rule2_successor = "FF"


    genotype = "X"


    for i in range(iterations):
        genotype = genotype.replace(rule1_predecessor, rule1_successor)
        genotype = genotype.replace(rule2_predecessor, rule2_successor)

    vt = rg.Point3d(0,0,0)

    vertices = []
    angles = []
    lines = []

    for c in genotype:
        if c == "+":
            # Turn right
            angle -= rotation
        elif c == "-":
            # Turn left
            angle += rotation
        elif c == "F":
            # Forward
            rad = math.radians(angle)
            next_vt = rg.Point3d(length*math.cos(rad) + vt.X, length*math.sin(rad) + vt.Y, 0)
            lines.append(rg.Line(vt, next_vt))
            
            vt = next_vt
            
        elif c == "[":
            # Save position
            vertices.append(vt)
            angles.append(angle)
        elif c == "]":
            # Restore position
            vt = vertices.pop()
            angle = angles.pop()
        
        
        
    L_system = lines
```

## Mola face

```python
    import mola
    from mola import module_rhino

    # Create an empty mesh
    m = mola.Mesh()

    # Define vertices
    a = mola.Vertex(0, 0, 0)
    b = mola.Vertex(15, 0, 0)
    c = mola.Vertex(15, 10, 0)
    d = mola.Vertex(0, 10, 0)

    # Add vertices to mesh
    vertices = [a, b, c, d]
    m.vertices = vertices

    # print(m.vertices)

    f = mola.Face([a,b,c,d])
    f.color = (0.6,0.6,0.6,1)
    m.faces.append(f)

    Mesh = module_rhino.display_mesh(m)
```

## Mola color
```python
    import mola

    # m = mola.construct_icosahedron(Radius)
    # Mesh = module_rhino.display_mesh(m)


    torus = mola.construct_torus(Radius, Radius2)

    mola.color_faces_by_curvature(torus.faces)
    # mola.color_faces_by_compactness(torus.faces)
    # mola.color_faces_by_area(torus.faces)

    Mesh = mola.module_rhino.display_mesh(torus)

    spheres = []
    for v in torus.vertices:
        radius = mola.math_map(v.z, -4, 4, 0.05, 0.5)
        s = mola.construct_sphere(radius, v.x, v.y, v.z,9, 9)
        temp = mola.module_rhino.display_mesh(s)
        spheres.append(temp)
        
    Spheres = spheres

```
