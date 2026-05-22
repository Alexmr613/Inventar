# app.py
import servicios
import archivos

def solicitar_numero(mensaje, tipo=float, no_negativo=True):
    """Función utilitaria para validar entradas numéricas por consola de forma segura."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if no_negativo and valor < 0:
                print("⚠️ El valor no puede ser negativo. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print(f"⚠️ Entrada inválida. Se esperaba un valor numérico de tipo {tipo.__name__}.")

def menu_estadisticas(inventario):
    stats = servicios.calcular_estadisticas(inventario)
    if not stats:
        print("\n📭 No hay datos suficientes para generar estadísticas.")
        return
        
    print("\n" + "📊 ESTADÍSTICAS DEL NEGOCIO " + "="*20)
    print(f"• Total de unidades en stock: {stats['unidades_totales']} uds.")
    print(f"• Valoración total del inventario: ${stats['valor_total']:,.2f}")
    print(f"• Producto más caro: {stats['mas_caro'][0]} (${stats['mas_caro'][1]:,.2f})")
    print(f"• Producto con mayor stock: {stats['mayor_stock'][0]} ({stats['mayor_stock'][1]} uds.)")
    print("="*48)

def ejecutar_sistema():
    inventario_memoria = []
    
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Consultar estadísticas")
        print("7. Guardar en archivo CSV")
        print("8. Cargar desde archivo CSV")
        print("9. Salir del programa")
        
        opcion = input("\nSeleccione una opción (1-9): ").strip()
        
        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                if not nombre.strip():
                    print("⚠️ El nombre no puede estar vacío.")
                    continue
                precio = solicitar_numero("Precio del producto: ", float)
                cantidad = solicitar_numero("Cantidad inicial: ", int)
                servicios.agregar_producto(inventario_memoria, nombre, precio, cantidad)
                
            elif opcion == "2":
                servicios.mostrar_inventario(inventario_memoria)
                
            elif opcion == "3":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                prod = servicios.buscar_producto(inventario_memoria, nombre)
                if prod:
                    print(f"\n🔍 Encontrado: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Stock: {prod['cantidad']}")
                else:
                    print("❌ Producto no registrado.")
                    
            elif opcion == "4":
                nombre = input("Ingrese el nombre del producto a actualizar: ")
                prod = servicios.buscar_producto(inventario_memoria, nombre)
                if prod:
                    print(f"Modificando '{prod['nombre']}' (Dejar vacío para mantener el valor actual)")
                    
                    precio_input = input(f"Nuevo precio (Actual: ${prod['precio']}): ").strip()
                    precio_nuevo = float(precio_input) if precio_input else None
                    if precio_nuevo is not None and precio_nuevo < 0:
                        print("⚠️ El precio no puede ser negativo. Operación cancelada.")
                        continue
                        
                    cant_input = input(f"Nueva cantidad (Actual: {prod['cantidad']}): ").strip()
                    cant_nueva = int(cant_input) if cant_input else None
                    if cant_nueva is not None and cant_nueva < 0:
                        print("⚠️ La cantidad no puede ser negativa. Operación cancelada.")
                        continue
                        
                    servicios.actualizar_producto(inventario_memoria, nombre, precio_nuevo, cant_nueva)
                else:
                    print("❌ El producto no existe.")
                    
            elif opcion == "5":
                nombre = input("Ingrese el nombre del producto a eliminar: ")
                servicios.eliminar_producto(inventario_memoria, nombre)
                
            elif opcion == "6":
                menu_estadisticas(inventario_memoria)
                
            elif opcion == "7":
                ruta = input("Ingrese el nombre o ruta del archivo para guardar (ej: datos.csv): ").strip()
                if not ruta:
                    ruta = "inventario.csv"  # Ruta por defecto
                archivos.guardar_csv(inventario_memoria, ruta)
                
            elif opcion == "8":
                ruta = input("Ingrese el nombre o ruta del archivo CSV a cargar: ").strip()
                productos_nuevos, filas_erroneas = archivos.cargar_csv(ruta)
                
                if productos_nuevos is not None:
                    print(f"\nSe leyeron correctamente {len(productos_nuevos)} productos.")
                    if filas_erroneas > 0:
                        print(f"⚠️ Se omitieron {filas_erroneas} filas inválidas por errores de formato o datos negativos.")
                    
                    # Preguntar política de guardado
                    while True:
                        decision = input("\n¿Desea sobrescribir el inventario actual por el del archivo? (S/N): ").strip().upper()
                        if decision == "S":
                            inventario_memoria = productos_nuevos
                            print("💥 Inventario actual reemplazado por completo.")
                            break
                        elif decision == "N":
                            # Aplicar política de fusión explicada al usuario
                            print("\n🔄 Fusionando... (Si el producto ya existe, se sumará el stock y se aplicará el precio nuevo)")
                            archivos.fusionar_inventarios(inventario_memoria, productos_nuevos)
                            print("✅ Fusión completada con éxito.")
                            break
                        else:
                            print("⚠️ Opción inválida. Responda 'S' para Sí o 'N' para No.")
                            
            elif opcion == "9":
                print("\n👋 ¡Gracias por usar el sistema de inventario! Saliendo de la sesión...")
                break
            else:
                print("❌ Opción no válida. Por favor, digite un número del 1 al 9.")
                
        except Exception as e:
            # Guardrail defensivo: cualquier error no controlado vuelve al menú sin romper el flujo
            print(f"\n⚠️ Ocurrió un error inesperado en el sistema: {e}")
            print("Volviendo al menú principal de forma segura...")

if __name__ == "__main__":
    ejecutar_sistema()