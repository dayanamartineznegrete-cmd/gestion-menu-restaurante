# Menú del restaurante

menu = [
    ["Hamburguesa", "Comida rápida", 18000],
    ["Pizza", "Comida rápida", 25000],
    ["Jugo Natural", "Bebida", 8000],
    ["Café Latte", "Bebida", 7000],
    ["Cheesecake", "Postre", 12000],
    ["Ensalada César", "Saludable", 15000]
]

print(menu)
print("\nMENÚ DEL RESTAURANTE")

for producto in menu:
    print(producto)
    print("\nMENÚ DEL RESTAURANTE")
print("----------------------")

for producto in menu:
    print("Producto:", producto[0])
    print("Categoría:", producto[1])
    print("Precio Base:", producto[2])
    print("----------------------")
    # Variables de promoción

categoria_objetivo = "Comida rápida"
umbral_precio = 15000
descuento = 15
print("\nPROMOCIONES")
print("----------------------")

for producto in menu:

    if producto[1] == categoria_objetivo:
        nuevo_precio = producto[2] - 15

    else:
        nuevo_precio = producto[2]

    print(producto[0], nuevo_precio)