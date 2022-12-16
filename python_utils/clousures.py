def make_repeater_of(n):

    def repeater(string):
        assert type(string)==str,"only enter strings"
        return string*n

    return repeater

def main():
    repeater5=make_repeater_of(5)
    print(repeater5("hola"))


if __name__=="__main__":
    main()