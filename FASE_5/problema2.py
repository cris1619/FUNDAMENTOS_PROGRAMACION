# ==========================================
# PROBLEMA 2 - PROMOCIÓN MENÚ RESTAURANTE
# ==========================================

# 1 - MOSTRAR EL MENÚ DEL RESTAURANTE

print("<------------- RESTAURANTE ---------------->")
print("<------------- MENÚ DISPONIBLE ------------>")
print("<-- COMIDA RAPIDA -->   <-- ITALIANA ----->")
print("<- Hamburguesa: $18000 > <- Pasta: $22000 >")
print("<- Pizza:       $25000 > <- Lasagna:$30000>")
print("<------------------------------------------>")
print("<----- SALUDABLE ----->  <---- BEBIDAS ---->")
print("<- Ensalada: $12000 --> <- Jugo: $8000 ---->")

# MATRIZ DEL MENÚ
menu = [
    ["Hamburguesa", "Comida Rapida", 18000],
    ["Pizza", "Comida Rapida", 25000],
    ["Ensalada", "Saludable", 12000],
    ["Pasta", "Italiana", 22000],
    ["Lasagna", "Italiana", 30000],
    ["Jugo Natural", "Bebida", 8000]
]

# VARIABLES DE PROMOCIÓN
categoria_objetivo = "Italiana"
umbral_precio = 20000
descuento = 0.15

# 2 - FUNCIÓN PARA CALCULAR EL PRECIO FINAL

def calcular_precio_final(categoria, precio_base):

    if categoria == categoria_objetivo and precio_base > umbral_precio:

        descuento_aplicado = precio_base * descuento
        precio_final = precio_base - descuento_aplicado

    else:

        descuento_aplicado = 0
        precio_final = precio_base

    return precio_final, descuento_aplicado


# 3 - MOSTRAR RESULTADOS

print("\n<--------- PROMOCIÓN DEL RESTAURANTE --------->")
print("<--- 15% DE DESCUENTO EN COMIDA ITALIANA ----->")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # LLAMAR LA FUNCIÓN
    precio_final, descuento_aplicado = calcular_precio_final(categoria, precio_base)

    # MOSTRAR INFORMACIÓN
    print("\n<------------- PRODUCTO ---------------->")
    print("<--- Nombre:", nombre)
    print("<--- Categoría:", categoria)
    print("<--- Precio Base: $", precio_base)

    if descuento_aplicado > 0:

        print("<--- Descuento Aplicado: $", descuento_aplicado)

    else:

        print("<--- No aplica descuento")

    print("<--- Precio Final: $", precio_final)
    print("<--------------------------------------->")


print("\n<------ PROMOCIÓN APLICADA EXITOSAMENTE ------>")
print("<------- REALIZADO POR CRISTIAN SOLANO ------->")
print("<---------- GRUPO NUMERO 213022A_2201 ---------->")