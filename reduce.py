import functools
n=(1,2,3,4)

result=functools.reduce(lambda counter,item:counter+item,n)

print(result)