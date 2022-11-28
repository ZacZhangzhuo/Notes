# MAS dfab - 3D Printing Architecture

## Goal

- Perforation
- Spatial structures
- Micro structures
- Ornament
- Material properties
- Architecture related
- Composition
- Connectivity
- Pattern generation
- Discrete architecture

![](9_MASdfab_3DPrintingArchitecture/1.jpg)

![](9_MASdfab_3DPrintingArchitecture/2.jpg)

![](9_MASdfab_3DPrintingArchitecture/3.jpg)

![](9_MASdfab_3DPrintingArchitecture/4.jpg)

![](9_MASdfab_3DPrintingArchitecture/5.jpg)

![](9_MASdfab_3DPrintingArchitecture/6.jpg)

## Joris lecture

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-16-09-50-34.png)

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-16-09-51-18.png)

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-16-09-54-42.png)
Above: to prevent the shrinkage and span of the 3D printing object

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-16-09-58-24.png)

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-16-10-00-49.png)

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-16-10-16-36.png)

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-16-10-32-07.png)
Above: Eggshell pavilion of MAS 2022

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-16-10-39-57.png)
Above: Eggshell pavilion of MAS 2022

![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-17-11-40-19.png)

## Arduino

- V = IR
- P = IV
- E = Pt
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-18-10-43-19.png)
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-18-10-45-38.png)
- Phototransistor can be measure if the object is in the front of it.
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-18-11-07-23.png)
- ![](9_MASdfab_3DPrintingArchitecture/x.jpg)
- ![](9_MASdfab_3DPrintingArchitecture/y.jpg)
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-18-14-10-09.png)

- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-19-15-58-54.png)
## Idea for the 'useless machine'
- One andiron that sends the red dot to the 'canvas', but also read the image of the canvas and change its position accordingly. This device can toy with the robots (like Eureka and Dummy). 
- https://youtu.be/ebLaWzjQ2Xg

## C++ Const and Static

- Const cannot be changed

```C++
    const int a = 10;
    a = 11; 
    // The code above will return error like 'cannot modify read-only' data.
```
- Static only gonna be linked internally inside the class (To be further studied)
  >**LINK** https://youtu.be/f3FVU-iwNuA

``` C++
    void loop{
        static int x = 0;
        x++;
        Serial.println(x);
    }//The output will be 1,2,3,4,5,6


    void loop{
        int x = 0;
        x++;
        Serial.println(x);
    }//The output will be 1,1,1,1,1,1

```


## 3D Printer Parameters

- Original prusa i3 MK2 with default nozzle of 0.4mm
- Extrudr PLA NX2, 1.75mm, 2500g


## UR rtd
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-28-13-43-52.png)
  
``` Python
    from compas.rpc import Proxy
    with Proxy('numpy') as np:
        pass
```
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-28-14-13-19.png)
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-28-14-39-29.png)
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-28-14-39-58.png)
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-28-14-40-23.png)
- ![](9_MASdfab_3DPrintingArchitecture/9_MASdfab_3DPrintingArchitecture_2022-11-28-14-41-30.png)