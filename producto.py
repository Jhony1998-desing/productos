productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Precio inválido. Por favor, introduce un número.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Cantidad inválida. Por favor, introduce un número entero.")
    
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print(f"Producto {nombre} añadido con éxito.")

def ver_productos():
    if not productos:
        print("No hay productos en el catálogo.")
    else:
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    try:
        indice = int(input("Introduce el número del producto que deseas actualizar: ")) - 1
        if 0 <= indice < len(productos):
            nombre = input("Introduce el nuevo nombre del producto (deja en blanco para no cambiar): ")
            precio = input("Introduce el nuevo precio del producto (deja en blanco para no cambiar): ")
            cantidad = input("Introduce la nueva cantidad del producto (deja en blanco para no cambiar): ")
    
            if nombre:
                productos[indice]["nombre"] = nombre
            if precio:
                try:
                    productos[indice]["precio"] = float(precio)
                except ValueError:
                    print("Precio inválido. No se actualizará el precio.")
            if cantidad:
                try:
                    productos[indice]["cantidad"] = int(cantidad)
                except ValueError:
                    print("Cantidad inválida. No se actualizará la cantidad.")
            print("Producto actualizado con éxito.")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("Entrada inválida. Debes introducir un número.")

def eliminar_producto():
    ver_productos()
    try:
        indice = int(input("Introduce el número del producto que deseas eliminar: ")) - 1
        if 0 <= indice < len(productos):
            producto_eliminado = productos.pop(indice)
            print(f"Producto {producto_eliminado['nombre']} eliminado con éxito.")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("Entrada inválida. Debes introducir un número.")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados con éxito.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
                productos.append(producto)
        print("Datos cargados con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Empezando con un catálogo vacío.")
    except ValueError:
        print("Error al cargar los datos. Por favor, revisa el archivo.")

def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
