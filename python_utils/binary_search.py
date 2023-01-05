objetive=int(input("Ingrese un numero entero => "))
epsilon=0.000001
low=0.0
high=max(1,0,objetive)
response=((high+low)/2)

while abs(response**2-objetive)>=epsilon:
    
    print(f'low={low}, high={high}, reponse={response}')

    if response**2<objetive:
        low=response
    else:
        high=response

    response=((high+low)/2)

print(f'La raiz cuadrada de: {objetive} es => {response}')