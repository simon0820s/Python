from traceback import print_tb


try:
    n=int(input("please enter the number, the system will give you the factorial: "))
    f=1
    while n>=1:
        f*=n
        n-=1
    print("")
except:
    print("only enter integer numeral caracters")

print('factorial = '+str(f))