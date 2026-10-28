productos = []

with open("datos.txt", "r") as archivo:
    for linea in archivo:
        productos.append(linea.strip().title())


def actualizar():
    with open("datos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(producto.strip().title() + "\n")


while True:
    opciones = input("A - Agregar\nR - Remover\nL - Listar\nS - Salir\n").strip().upper()

    match opciones:
        case "S":
            break
        case "A":
            agregar = input("\nagregar: ")
            productos.append(agregar.strip().title())

            actualizar()

        case "R":
            remover = input("\nRemover: ")
            productos.remove(remover.strip().title())

            actualizar()

        case "L":
            print(productos)


