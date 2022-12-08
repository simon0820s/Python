import random


def main():
    #dicciónario nombres-edades
    names = ['nico', 'simon', "santi"]
    new_dict = {names[i]:random.randint(1,10) for i in range(len(names))}
    print(new_dict)
    print('')
    
    #dicciónario del 1-100 con valores cuadrados de cara una de los numeros solo si estos son divisibles entre 3
    dict={i:i**2 for i in range(1,101) if i%3==0}
    print(dict)

if __name__=='__main__':
    main()