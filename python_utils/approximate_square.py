objetive=int(input("ingrese un numero entero => "))
epsilon=0.01
paso=epsilon**2
respuesta=0.0

while abs(respuesta**2-objetive)>=epsilon and respuesta <=objetive:
    print(abs(respuesta**2-objetive),respuesta)
    respuesta+=paso

if abs(respuesta**2-objetive)>=epsilon:
    print(f'No se encontro la raiz de: {objetive}')
else:
    print(f'La raiz cuadrada de: {objetive} = {respuesta}')