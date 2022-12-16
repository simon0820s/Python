set_a={'col','mex','per'}
set_b={'arg','chi','mex'}

#Union
set_c=set_a.union(set_b)
print(set_c)

#Interseccion
set_c = set_a.intersection(set_b)
print(set_c)

#Diferencia
set_c=set_a.difference(set_b)
print(set_c)

#Diferencia Simetrica
set_c=set_a.symmetric_difference(set_b)
print(set_c)