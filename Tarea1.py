# La empresa en la que trabajas recibe una gran cantidad de materias primas
# y otros productos en su inventario, los cuales son registrados y manejados
# en hojas de papel que describen nombres, cantidades, precios, tipos y tamaños
# de cada producto que entra y sale. Recientemente se perdieron algunas hojas y
# se tomó la decisión de digitalizar este proceso. Dado esto, se te pide que
# desarrolles un programa en Python, en el cual, la persona encargada de
# registrar entradas y salidas de inventarios, mediante la terminal del sistema
# operativo pueda hacer estos registros fácilmente.
# La tarea se deberá llevar a cabo utilizando funciones para añadir nuevos artículos,
# actualizar cantidades y buscar artículos específicos basándose en varios criterios.
# Se deberán utilizar funciones lambda para ordenar el inventario en función de diferentes
# atributos, como ordenar los artículos por nombre, cantidad o precio. Además, se deberán
# emplear funciones anidadas para gestionar operaciones complejas, como generar informes
# de inventario o calcular el valor total del inventario.
# Se deberá subir este archivo de Python a un repositorio Github, junto con un archivo README.md
# que explique cómo utilizar el programa.
# Se evaluará el uso de funciones y funciones lambda para agregar (con diferentes datos incluyendo
# fecha con la paquetería datetime), editar, leer, y borrar productos del inventario, que todo
# funcione correctamente y que contenga el archivo README
# Adicionalmente hacer 3 funciones mas a gusto propio

from datetime import datetime

inventario = []


def validar_agregar(nombre):
    band = True
    for articulo in inventario:
        if articulo.get("nombre") == nombre:
            band = False
    return band


def agregar_nuevo_articulo():
    nombre = input("Introduce el nombre: ")
    if nombre.strip() != "" and validar_agregar(nombre):
        cantidad = int(input("Introduce la cantidad: "))
        precio = float(input("Introduce el precio: "))
        tipo = input("Introduce el tipo: ")
        tamano = input("Introduce el tamaño: ")
        date=datetime.today().strftime('%Y-%m-%d')
        articulo = {
            "id": len(inventario) + 1,
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "tipo": tipo,
            "tamano": tamano,
            "last_update":date
        }
        inventario.append(articulo)
        print(f"El artículo {nombre}, se agrego satisfactoriamente.")
    else:
        print("El artículo ya se encuentra registrado o el nombre se encuentra vacío.")


def actualizar_articulo():
    nombre = input("Introduce el nombre del artículo que se actualizará: ")
    for articulo in inventario:
        if articulo.get("nombre") == nombre:
            articulo["cantidad"] = input("Introduce la nueva cantidad: ")
            articulo["precio"] = input("Introduce el nuevo precio: ")
            articulo["tipo"] = input("Introduce el nuevo tipo: ")
            articulo["tamano"] = input("Introduce el nuevo tamaño: ")
            articulo["last_update"]=datetime.today().strftime('%Y-%m-%d')
            print(f"El artículo {nombre}, se actualizo correctamente.")


def buscar_articulos():
    option = int(
        input("Buscar por: \n1.Nombre\n2.Tamaño\n3.Tipo\n4.Fecha\nSelecciona una opción:")
    )
    options = {
        1: lambda: buscarPorNombre(),
        2: lambda: buscarPorTam(),
        3: lambda: buscarPorTipo(),
        4: lambda: buscarPorFecha(),
    }
    options.get(option, lambda: print("Opcion no válida"))()


def buscarPorNombre():
    nombre = input("Introduce el nombre: ")
    filtered_articulos = list(
        filter(
            lambda articulo: nombre.lower() in articulo.get("nombre").lower(),
            inventario,
        )
    )
    print("Los articulos encontrados: ")
    imprimir_articulos(filtered_articulos)


def buscarPorTam():
    tam = input("Introduce el tamaño: ")
    filtered_articulos = list(
        filter(
            lambda articulo: tam.lower() in articulo.get("tamano").lower(), inventario
        )
    )
    print("Los articulos encontrados: ")
    imprimir_articulos(filtered_articulos)


def buscarPorTipo():
    tipo = input("Introduce el tipo: ")
    filtered_articulos = list(
        filter(
            lambda articulo: tipo.lower() in articulo.get("tipo").lower(), inventario
        )
    )
    print("Los articulos encontrados: ")
    imprimir_articulos(filtered_articulos)

def buscarPorFecha():
    fecha = input("Introduce la fecha: ")
    filtered_articulos = list(
        filter(
            lambda articulo: fecha.lower() in articulo.get("last_update").lower(), inventario
        )
    )
    print("Los articulos encontrados: ")
    imprimir_articulos(filtered_articulos)


def ordenar_articulos():
    option = int(
        input("Ordenar por: \n1.Nombre\n2.Tamaño\n3.Tipo\nSelecciona una opción:")
    )
    options = {
        1: lambda: sorted(inventario, key=lambda articulo: articulo.get("nombre")),
        2: lambda: sorted(inventario, key=lambda articulo: articulo.get("tamano")),
        3: lambda: sorted(inventario, key=lambda articulo: articulo.get("tipo")),
    }
    data = options.get(option, lambda: [])()
    imprimir_articulos(data)


def borrar_articulo():
    nombre = input("Introduce el nombre: ")
    ind = -1
    for index, articulo in enumerate(inventario):
        if nombre == articulo.get("nombre"):
            inventario.pop(index)
            print("El elemento se elimino correctamente. ")


def diminuir_cantidad_articulo():
    nombre = input("Introduce el nombre: ")
    cantidad = int(input("Introduce la cantidad a disminuir: "))
    for articulo in inventario:
        if nombre == articulo.get("nombre"):
            articulo["cantidad"] = articulo.get("cantidad") - cantidad
            print("La cantidad se disminuyo correctamente.")


def aumentar_cantidad_articulo():
    nombre = input("Introduce el nombre: ")
    cantidad = int(input("Introduce la cantidad que se aumentará: "))
    for articulo in inventario:
        if nombre == articulo.get("nombre"):
            articulo["cantidad"] = articulo.get("cantidad") + cantidad
            print("La cantidad se aumento correctamente.")


def calcular_total_inventario():
    total = 0
    for articulo in inventario:
        total += articulo.get("cantidad")
    print(f"En el inventario hay {total} artículos.")


def imprimir_articulos(articulos):
    print(
        "| {:10} | {:15} | {:10} | {:10} | {:10} | {:10} | {:10}".format(
            "ID", "NOMBRE", "TIPO", "TAMAÑO", "CANTIDAD", "PRECIO","FECHA"
        )
    )
    for articulo in articulos:
        print(
            "| {:10} | {:15} | {:11}| {:10} | {:10} | {:10} | {:10}".format(
                articulo.get("id"),
                articulo.get("nombre"),
                articulo.get("tipo"),
                articulo.get("tamano"),
                articulo.get("cantidad"),
                articulo.get("precio"),
                articulo.get("last_update"),
            )
        )
        print("\n")
        
def generar_archivo_txt():
    separador="+"+"-"*100+"+"
    archivo= open("inventario_reporte.txt","w")
    archivo.write("Control de inventario")
    archivo.write(separador)
    archivo.write("\n")
    archivo.write( "| {:10} | {:15} | {:10} | {:10} | {:10} | {:10} | {:10}".format(
            "ID", "NOMBRE", "TIPO", "TAMAÑO", "CANTIDAD", "PRECIO","FECHA"
        ))
    archivo.write("\n")
    archivo.write(separador)
    archivo.write("\n")
    for articulo in inventario:
        archivo.write("| {:10} | {:15} | {:11}| {:10} | {:10} | {:10} | {:10}".format(
                articulo.get("id"),
                articulo.get("nombre"),
                articulo.get("tipo"),
                articulo.get("tamano"),
                articulo.get("cantidad"),
                articulo.get("precio"),
                articulo.get("last_update"),
            ))
        archivo.write("\n")
    archivo.write(separador)
    archivo.close()


def get_message_choice(option):
    msg = "La opción no se encontro."
    if option == 11:
        msg = "Has salido del control de inventario."
    return msg


def menu_principal():
    choice = 0
    while choice != 11:
        print("\n --- Control de inventarios ---")
        print("1. Agregar nuevo artículo.")
        print("2. Actualizar datos de un artículo.")
        print("3. Buscar un artículo.")
        print("4. Ordenar artículos.")
        print("5. Borrar articulo.")
        print("6. Disminuir cantidad de un articulo.")
        print("7. Aumentar cantidad de un articulo")
        print("8. Calcular total del inventario.")
        print("9. Mostrar inventario.")
        print("10. Generar reporte.")
        print("11. Salir")
        choice = int(input("Introduce una opción: "))

        options = {
            1: lambda: agregar_nuevo_articulo(),
            2: lambda: actualizar_articulo(),
            3: lambda: buscar_articulos(),
            4: lambda: ordenar_articulos(),
            5: lambda: borrar_articulo(),
            6: lambda: diminuir_cantidad_articulo(),
            7: lambda: aumentar_cantidad_articulo(),
            8: lambda: calcular_total_inventario(),
            9: lambda: imprimir_articulos(inventario),
            10:lambda:generar_archivo_txt()
        }
        options.get(choice, lambda: print(get_message_choice(choice)))()


menu_principal()
