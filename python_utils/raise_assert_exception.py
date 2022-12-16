def main():
    try:
        n=int(input('enter your month of birth: '))
        assert n>0,"Enter only positive numbers"
    except ValueError:
        print("only enter numeral caracters")
    print("the program has fisnished")

    
if __name__=='__main__':
    main()