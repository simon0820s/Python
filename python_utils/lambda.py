#Corrector suma
n=int(input("ingrese 2+2: "))
r=lambda n:n==4
print(r(n))

#Incremento
i = lambda x:x+1
print(i(2))

#
full_name=lambda name,lastName:f'Full name = {name.title()} {lastName.title()}'

text=full_name('Simón','Arboleda')
print(text)