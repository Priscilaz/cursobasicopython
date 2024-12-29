"""mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
#otro_set = {1,2,3}
#print(type(otro_set))
#Esto no es valido
#print(mi_set[0])
print(len(mi_set))
print(2 in mi_set)"""

##--Union de Sets
s1 = {1,2,3}
#s2 = {3,4,5}
#s3 = s1.union(s2)
#print(s3)
s1.add(6)
s1.remove(2)
print(s1)
#Casi igual que el remove, pero si el elemento no
#existe, no me da error
#s1.discard(5)
#Pop elimina un elemento cualquiera, no en un orden especifico
s1.pop()
print(s1)
#vaciar el set
s1.clear()
print(s1)
