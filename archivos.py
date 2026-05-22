# archivos.py
import csv
from servicios import buscar_producto

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario actual en un archivo CSV.
    """
    if not inventario:
        print("⚠️ El inventario está vacío. No hay datos para guardar.")
        return False
        
    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ["nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            if incluir_header:
                escritor.writeheader()
                
            for p in inventario:
                escritor.writerow(p)
                
        print(f"💾 ¡Inventario guardado con éxito en: {ruta}!")
        return True
        
    except PermissionError:
        print(f"❌ Error de permisos: No se puede escribir en '{ruta}'. Verifica que el archivo no esté abierto.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al guardar el archivo: {e}")
    return False

def cargar_csv(ruta):
    """
    Lee y valida un archivo CSV. 
    Retorna una tupla: (lista_de_productos_validos, contador_errores)
    """
    productos_cargados = []
    filas_invalidas = 0
    
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            # Forzamos la lectura usando el lector básico para validar la estructura exacta
            lector = csv.reader(archivo)
            
            # Validar si el archivo está vacío
            try:
                header = next(lector)
            except StopIteration:
                print("❌ El archivo seleccionado está completamente vacío.")
                return None, 0
                
            # Validar estructura del encabezado (eliminando espacios y pasándolo a minúsculas)
            header_limpio = [h.strip().lower() for h in header]
            if header_limpio != ["nombre", "precio", "cantidad"]:
                print("❌ Formato de encabezado inválido. Se esperaba: nombre,precio,cantidad")
                return None, 0
                
            # Procesar filas del cuerpo
            for num_fila, fila in enumerate(lector, start=2):
                # Validar que tenga exactamente 3 columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                    
                nombre, precio_str, cantidad_str = fila
                nombre = nombre.strip()
                
                # Validar campos vacíos
                if not nombre or not precio_str or not cantidad_str:
                    filas_invalidas += 1
                    continue
                
                try:
                    precio = float(precio_str)
                    cantidad = int(cantidad_str)
                    
                    # Validar no negativos
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue
                        
                    productos_cargados.append({
                        "nombre": nombre.capitalize(),
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except ValueError:
                    # Captura errores de conversión de tipos (ej: letras en precio)
                    filas_invalidas += 1
                    continue
                    
        return productos_cargados, filas_invalidas

    except FileNotFoundError:
        print(f"❌ Error: El archivo en la ruta '{ruta}' no existe.")
    except UnicodeDecodeError:
        print("❌ Error de codificación: Asegúrate de que el archivo sea un CSV válido en formato UTF-8.")
    except Exception as e:
        print(f"❌ Error inesperado al cargar el archivo: {e}")
        
    return None, 0

def fusionar_inventarios(inventario_actual, productos_nuevos):
    """
    Fusiona el inventario en memoria con los nuevos productos cargados.
    Política: Si ya existe el nombre, se suma la cantidad y se actualiza al nuevo precio.
    """
    for p_nuevo in productos_nuevos:
        p_existente = buscar_producto(inventario_actual, p_nuevo["nombre"])
        if p_existente:
            p_existente["cantidad"] += p_nuevo["cantidad"]
            p_existente["precio"] = p_nuevo["precio"] # Actualiza al nuevo precio
        else:
            inventario_actual.append(p_nuevo)