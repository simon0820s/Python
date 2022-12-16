def palindrome(word):
    word=word.replace(" ","")
    word=word.lower()
    wordInvert=word[::-1]
    if word==wordInvert:
        return True
    else:
        return False


def main():
    word=input("enter a word and the system tell you if it word is palindrome: ")
    c=palindrome(word)
    if c==True:
        print("your word is palindrome")
    else:
        print("your word no is palindrome")


if __name__=="__main__":
    main()