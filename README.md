# Inventario.py
# 📦 Ejecución del algoritmo de registro de productos

Este programa en Python permite ingresar información de un producto mediante consola, validando correctamente los datos introducidos por el usuario.
El sistema solicita:

* Precio del producto
* Nombre del producto
* Cantidad

El programa utiliza estructuras `while` y manejo de excepciones `try/except` para validar que los datos ingresados sean correctos antes de continuar.

---

# 🚀 Cómo clonar el repositorio

Sigue estos pasos para obtener el proyecto en tu ordenador.

### 1. Clonar el repositorio

Abre una terminal o consola y ejecuta:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

### 2. Acceder a la carpeta del proyecto

```bash
cd tu-repositorio
```

---

# ▶️ Cómo ejecutar el programa

### 1. Verificar que Python esté instalado

Puedes comprobarlo con:

```bash
python --version
```

o

```bash
python3 --version
```

Si no lo tienes instalado, descárgalo desde la página oficial de Python.

---

### 2. Ejecutar el script

Dentro de la carpeta del proyecto ejecuta:

```bash
python main.py
```

o

```bash
python3 main.py
```

*(Reemplaza `main.py` por el nombre del archivo donde está el algoritmo si es diferente).*

---

# 🧠 Funcionamiento del algoritmo

El programa realiza las siguientes acciones:

1. Solicita el **precio del producto** y valida que sea un número decimal.
2. Solicita el **nombre del producto**.
3. Solicita la **cantidad** y valida que sea un número entero.
4. Calcula el **costo total** mediante la fórmula:

```
costo_total = precio * cantidad
```

5. Finalmente muestra en pantalla:

* Nombre del producto
* Precio
* Cantidad
* Total a pagar

Si el usuario introduce un valor incorrecto, el programa mostrará un mensaje de error y volverá a solicitar el dato.

---

# 💻 Ejemplo de uso

```
Digite su precio: 10.5
Digite el nombre del producto:
Laptop
Digite la cantidad a ingresar: 2

Producto Laptop Precio 10.5 Cantidad 2 Total 21.0
```

---

# 📌 Notas

* El programa utiliza bucles `while` para asegurar que los datos introducidos sean válidos.
* Se emplea `try/except` para evitar errores cuando el usuario introduce valores incorrectos.
