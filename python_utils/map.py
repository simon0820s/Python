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

#Double iteration
n1=(1,2,3,4)
n2=(5,6,7)
print("double iteration")
print('n1 = '+str(n1))
print('n2 = '+str(n2))
result=list(map(lambda x,y: x+y,n1,n2))
print('result = '+str(result))
