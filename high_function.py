#Normal
def increment(x):
    return x+1

def high_function(x,func):
    return x+func(x)

result=high_function(2,increment)
print(result)

#Lambda
high_functionLambda=lambda x,func: x+func(x)

resultLambda=high_functionLambda(2,lambda x:x+1)

print(resultLambda)