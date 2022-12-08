def main():
    #lista generada con comperhentions
    numbers=[element for element in range(1,11)]
    print(numbers)
    print('')

    #lista con elementos hasta el numero 10.000 solo multiplos de 4,6,9
    list=[i for i in range(10000) if i%4==0 and i%6==0 and i%9==0]
    print(list)
if __name__=='__main__':
    main()