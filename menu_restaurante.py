
# función
def calcular_precio_final(precio_base, descuento):
    precio_final = precio_base * (1 - descuento / 100)
    return precio_final


# menú del restaurante
menu = [
    ["Hamburguesa", "Comida rápida", 18000],
    ["Pizza", "Comida rápida", 25000],
    ["Perro Caliente", "Comida rápida", 12000],
    ["Salchipapa", "Comida rápida", 16000],
    ["Jugo Natural", "Bebida", 8000],
    ["Café Latte", "Bebida", 7000],
    ["Limonada", "Bebida", 6000],
    ["Cheesecake", "Postre", 12000],
    ["Brownie", "Postre", 9000],
    ["Ensalada César", "Saludable", 15000]
]

# mostrar matriz
print(menu)

print("\nMENÚ DEL RESTAURANTE")
print("----------------------")

# mostrar menú
for producto in menu:
    print(producto[0], producto[1], producto[2])

# variables
categoria_objetivo = "Comida rápida"
umbral_precio = 15000
descuento = 15

print("\nPROMOCIONES")
print("----------------------")

# aplicar lógica
for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    if categoria == categoria_objetivo and precio_base > umbral_precio:
        precio_final = calcular_precio_final(precio_base, descuento)
    else:
        precio_final = precio_base

    print(nombre, "Base:", precio_base, "Final:", int(precio_final))