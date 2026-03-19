
inv=[]
cont = "s" 

def agregar_producto():
        dicc= {"nombre" :"", # Creacion de diccionario
        "precio": 0,
        "cantidad" : 0 }

        
        nombre =input("digite el nombre del producto")
        if isinstance(nombre, int)== True: # Validacion de datos
            print("Digite un nombre valido ")
        
            
        precio = input("digite el precio del producto")
        if isinstance(precio, str)== True : 
            print("Digite un precio validos ")
        cantidad = input("digite la cantidad a registrar ") #Creacion del producto
        if isinstance(cantidad, str) == True : 
            print("Digite una cantidad valida ")

        dicc["nombre"] = nombre #Integrar el producto al diccionario
        dicc["precio"] = precio
        dicc["cantidad"]= cantidad
        inv.append(dicc)
        

        print(dicc)
        return dicc
def mostrar_inventario():
  for i in range(len(inv)): # Mostrar el inventario
            print(inv[i])
def calcular_estadisticas():
  cont2= 0
  cont3 = 0
  for i in range(len(inv)):
     cont2 = cont2 + inv[i].pop("precio")
     cont3 = cont3 + inv[i].pop("cantidad")# Calcular el total de la sumatoria del precio * cantidad

     print(cont2 * cont3)
  return cont2 * cont3
 

while cont == "s" :
    
   
    print("Bienvenido al menu de la historia de usuario")#Menu de usuario
    print("Agregar producto (1)")
    print("Mostrar inventario (2)")
    print("Calcular estadisticas (3)")
    print("Salir (4)")
    op= int(input("Digite la opcion a elegir "))

    if op == 1:
       agregar_producto()#Invocacion de la funcion


    
    if op == 2:
       mostrar_inventario()#Invocacion de la funcion

    
    if op == 3:
        calcular_estadisticas()#Invocacion de la funcion
   



    
    if op == 4:
        break
   


    
    


