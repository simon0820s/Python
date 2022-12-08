v1=[1,2,3,4,5]
print('numbers'+' = '+str(v1))
#Normal modify
v2=[]
for i in v1:
    v2.append(i*2)
print("Normal modify: "+str(v2))

#Map modify
v2map=list(map((lambda i:i*2),v1))
print("Map modify: "+str(v2map))