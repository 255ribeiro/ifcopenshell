import sys
import ifcopenshell as ifc
import pandas as pd


sys.path.append(r'C:\Users\ferra\AppData\Roaming\Blender Foundation\Blender\2.93\scripts\addons\blenderbim')
import ifcopenshell as ifc
f = ifc.open('202103162102_cira.ifc')
print(f)