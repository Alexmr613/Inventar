
while True :
    try:
    
            
      precio = float(input("Digite su precio " )) # Validacion precio
      break

    except ValueError :
        print("Por favor ingrese un num valido")

while True : 
    try :
 
      nombre = str(input("Digite el nombre del producto:\n ")) # Validacion nombre
      break
    except ValueError :
        print("Por favor ingrese un nombre valido")


while True : 
    try:
    
     cantidad = int(input("Digite la cantidad a ingresar ")) # Validacion cantidad
     break
    except ValueError:
       print("Digite una cantidad valida")
costototal= (precio * cantidad)

print("Producto ", nombre, "Precio " , precio , "Cantidad ", cantidad, "Total " , costototal) # Muestra el valor total y las caracteristicas del producto


#ESTE Programa funciona mediante validaciones por el bucle while, mientras no entre el tipo de dato correcto el programa te lo indicara y te exigira nuevamente el dato correcto



