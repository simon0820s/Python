import random
options=('piedra','papel','tijera')

user_option= input("piedra, papel o tijera => ")
user_option=user_option.lower()
computer_option=random.choice(options)

print('User Option =>', user_option)
print('Computer option =>',computer_option)

if user_option==computer_option:
    print("Empate!!")

elif user_option == "piedra":
    if computer_option=="tijera":
        print("piedra gana a tijera")
        print("user gana!!")
    else:
        print("papel gana a piedra")
        print("computer gana")

elif user_option == "papel":
    if computer_option=="piedra":
        print("papel gana a piedra")
        print("user gana!!")
    else:
        print("tijeras gana a papel")
        print("computer gana")
    
elif user_option == "tijera":
    if computer_option=="papel":
        print("tijeras gana a papel")
        print("user gana!!")
    else:
        print("piedra gana a tijeras")
        print("computer gana")
