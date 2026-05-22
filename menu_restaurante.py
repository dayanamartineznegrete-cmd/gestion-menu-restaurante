
   # MENÚ DEL RESTAURANTE

menu = [
    ["Hamburguesa", "Comida rápida", 18000],
    ["Pizza", "Comida rápida", 25000],
    ["Jugo Natural", "Bebida", 8000],
    ["Café Latte", "Bebida", 7000],
    ["Cheesecake", "Postre", 12000],
    ["Ensalada César", "Saludable", 15000]
]

# Mostrar la matriz original
print(menu)

print("\nMENÚ DEL RESTAURANTE")
print("----------------------")

# Mostrar el menú de forma ordenada
for producto in menu:
    print("Producto:", producto[0])
    print("Categoría:", producto[1])
    print("Precio:", producto[2])
    print("----------------------")

# Variables para promoción
categoria_objetivo = "Comida rápida"
descuento = 15

print("\nPROMOCIONES")
print("----------------------")

# Aplicar descuento solo a una categoría
for producto in menu:

    if producto[1] == categoria_objetivo:
        nuevo_precio = producto[2] * (1 - descuento / 100)
        print(producto[0], "->", int(nuevo_precio))
    else:
        print(producto[0], "->", producto[2])