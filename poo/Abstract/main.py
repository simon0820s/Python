from student import Student


def run():
    profession=input("Mateo is a good boy he has 20 years old, what is his profession? ")
    mateo=Student(name="Mateo",age=20,profession=profession)
    print(mateo.say_my_profession())

if __name__=='__main__':
    run()