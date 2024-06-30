from numpy import *
from lab_1 import g
h = 100
a= 45
b = 35
v = sqrt((g * tan(b)**2) / (2 * cos(a)**2 * (1 - tan(b) * tan(a))))
print(v)