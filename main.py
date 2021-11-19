import sqlite3
INV = "inventario.db"


def obtener_conexion():
    return sqlite3.connect(INV)


def crear_tablas():
    tablas = [
        """
        CREATE TABLE IF NOT EXISTS inventario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            articulo TEXT NOT NULL,
            cantidad INTEGER
        );
        """
    ]
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for tabla in tablas:
        cursor.execute(tabla)


def principal():
    crear_tablas()
    menu = """
a) Agregar nuevo articulo
b) Editar articulo existente
c) Eliminar articulo existente
d) Ver listado de articulos
f) Salir
Elige: """
    eleccion = ""
    while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            articulo = input("Ingresa el articulo: ")
            # Comprobar si no existe
            posible_cantidad = buscar_articulo(articulo)
            if posible_cantidad:
                print(f"El articulo '{articulo}' ya existe")
            else:
                cantidad = input("Ingresa la cantidad: ")
                agregar_articulo(articulo, cantidad)
                print("Articulo agregado")
        if eleccion == "b":
            articulo = input("Ingresa el articulo que quieres editar: ")
            nueva_cantidad = input("Ingresa la nueva cantidad: ")
            editar_articulo(articulo, nueva_cantidad)
            print("Articulo actualizado")
        if eleccion == "c":
            articulo = input("Ingresa el articulo a eliminar: ")
            eliminar_articulo(articulo)
        if eleccion == "d":
            articulos = obtener_articulos()
            print("=== Lista de articulos ===")
            for articulo in articulos:
                print(articulo[0])
        if eleccion == "e":
            articulo = input(
                "Ingresa el articulo del cual quieres saber el cantidad: ")
            cantidad = buscar_articulo(articulo)
            if cantidad:
                print(f"El cantidad de '{articulo}' es:\n{cantidad[0]}")
            else:
                print(f"Articulo '{articulo}' no encontrado")


def agregar_articulo(articulo, cantidad):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO inventario(articulo, cantidad) VALUES (?, ?)"
    cursor.execute(sentencia, [articulo, cantidad])
    conexion.commit()


def editar_articulo(articulo, nueva_cantidad):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "UPDATE inventario SET cantidad = ? WHERE articulo = ?"
    cursor.execute(sentencia, [nueva_cantidad, articulo])
    conexion.commit()


def eliminar_articulo(articulo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM inventario WHERE articulo = ?"
    cursor.execute(sentencia, [articulo])
    conexion.commit()


def obtener_articulos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT articulo AND cantidad FROM inventario"
    cursor.execute(consulta)
    return cursor.fetchall()


def buscar_articulo(articulo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT cantidad FROM inventario WHERE articulo = ?"
    cursor.execute(consulta, [articulo])
    return cursor.fetchone()


if __name__ == '__main__':
    principal()
