n=tuple(reversed(range(1,11)))

def run(n):
    response=[]

    for i in n:
        response.append(fibonacci(i))
    
    response=tuple(reversed(response))
    print(response)

def fibonacci(i):

        if i<=1:
            return i
            
        else:
            return(fibonacci(i-1)+fibonacci(i-2))

if __name__=='__main__':
    run(n)