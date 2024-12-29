"""mi_tuple = (1,2,(3,10,20),4)
t = (1, 2,55, "e")
print(mi_tuple)
print(mi_tuple[2][0])
mi_tuple = list(mi_tuple)

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))
#print(t)"""
from operator import length_hint

t = (1,2,3,1)
#x,y,z = t
#print(x,y,z)
print(t.count(1))
print(t.index(2))