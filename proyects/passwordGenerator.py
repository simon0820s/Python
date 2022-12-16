import random   
def generatePassword():
    up=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"] 
    low=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    simb=["!","#","&","?","¿","$"]
    num=["1","2","3","4","5","6","7","8","9","10"]
    caracters=up+low+simb+num
    password=[]
    for i in range(10):
        rand=random.choice(caracters)
        password.append(rand)
    password=''.join(password)
    return password


def main():
    password=generatePassword()
    print('your new password is: '+password)

if __name__=='__main__':
    main()