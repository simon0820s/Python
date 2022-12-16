def cousin(number):
    c=True
    for i in range(1,number+1):
        if i==1 or i==number:
            continue
        if number%i==0:
            c=False
    return c


number=int(input("please enter an number and system tell you if this number is cousin: "))
if cousin(number):
    print("is cousin")
else:
    print("no is cousin")