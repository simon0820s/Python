def main():
    #lista con elementos hasta 5 digitos, multiplos de 4,6,9
    list=[i for i in range(10000) if i%4==0 and i%6==0 and i%9==0]
    print(list)
if __name__=='__main__':
    main()