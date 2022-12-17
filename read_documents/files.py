file = open('./read_documents/text.txt','r')
#Lectura automatica
#print(file.read())
#Lectura manual
""" print(file.readline())
print(file.readline())
print(file.readline()) """

#Cerrar archivo
#file.close()

#Para leer un archivo muy grande completo es mejor usar for
""" for line in file:
    print(line)
file.close() """

#Esta sentencia cierra el archivo automaticamente al finalizar el bloque
#Escribir en archivo
with open('./read_documents/text.txt','w+') as file:
    for i in range(10,21):
        for line in file:
            print(line)
        file.write("\n")
        file.write(str(i))
    

