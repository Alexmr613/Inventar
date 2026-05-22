# servicios.py

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario en memoria.
    
    :param inventario: list, lista de diccionarios de productos.
    :param nombre: str, nombre único del producto.
    :param precio: float, precio unitario.
    :param cantidad: int, stock inicial.
    """
    # Normalizamos el nombre para evitar duplicados por mayúsculas/minúsculas
    nombre_limpio = nombre.strip().capitalize()
    
    # Validar si ya existe
    if buscar_producto(inventario, nombre_limpio):
        print(f"⚠️ El producto '{nombre_limpio}' ya existe. Usa la opción de actualizar.")
        return False
        
    producto = {
        "nombre": nombre_limpio,
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    inventario.append(producto)
    print(f"✅ Producto '{nombre_limpio}' agregado exitosamente.")
    return True

def mostrar_inventario(inventario):
    """Muestra de forma formateada todos los productos del inventario."""
    if not inventario:
        print("\n📭 El inventario está vacío.")
        return

    print("\n" + "="*45)
    print(f"{'PRODUCTO':<20} | {'PRECIO':<10} | {'STOCK':<8}")
    print("="*45)
    for p in inventario:
        print(f"{p['nombre']:<20} | ${p['precio']:<9.2f} | {p['cantidad']:<8}")
    print("="*45)

def buscar_producto(inventario, nombre):
    """
    Busca un producto por su nombre.
    
    :return: dict con el producto si lo encuentra, None en caso contrario.
    """
    nombre_buscado = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].lower() == nombre_buscado:
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o la cantidad de un producto existente.
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"❌ No se encontró el producto '{nombre}'.")
        return False
    
    if nuevo_precio is not None:
        producto["precio"] = float(nuevo_precio)
    if nueva_cantidad is not None:
        producto["cantidad"] = int(nueva_cantidad)
        
    print(f"🔄 Producto '{producto['nombre']}' actualizado correctamente.")
    return True

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario por su nombre."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print(f"🗑️ Producto '{producto['nombre']}' eliminado del inventario.")
        return True
    print(f"❌ No se encontró el producto '{nombre}'.")
    return False

def calcular_estadisticas(inventario):
    """
    Calcula métricas clave del inventario actual.
    
    :return: dict con las estadísticas calculadas o None si está vacío.
    """
    if not inventario:
        return None
        
    # Uso de Lambda opcional para calcular el subtotal de un producto (precio * cantidad)
    subtotal = lambda p: p["precio"] * p["cantidad"]
    
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    
    # Encontrar máximos usando max() con key explicativo
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }