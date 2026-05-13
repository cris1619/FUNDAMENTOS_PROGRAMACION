#1 - MOSTRAR LOS PRODUCTOS Y PRECIOS

print("<----------------- PANADERIA --------------->")
print("<------------ LISTA DE PRODUCTOS ----------->")
print("<------ PANES ------>  <----- PASTELES ----->")
print("<- Integral: $2.000 >  <- Chocolate: $6.000 >")
print("<- Frances:  $3.000 >  <- Manzana:   $5.000 >")
print("<- Queso:    $1.000 >")

# PRECIOS
Integral = 2000
Frances = 3000
Queso = 1000
Chocolate = 6000
Manzana = 5000

#2 - INGRESAR PRODUCTO Y CANTIDAD
producto = input("<--- Ingrese el nombre del producto: ").lower()
cantidad = int(input("<--- Ingrese la cantidad: "))

#3 - CALCULAR EL TOTAL A PAGAR
if producto == "integral":
    total = cantidad * Integral
elif producto == "frances":
    total = cantidad * Frances
elif producto == "queso":
    total = cantidad * Queso
elif producto == "chocolate":
    total = cantidad * Chocolate
elif producto == "manzana":
    total = cantidad * Manzana
else:
    print("<--- Producto no válido")
    total = 0

#4 - APLICAR DESCUENTO
print("<------------- RESUMEN DE COMPRA ------------>")
print("<--- Producto:", producto.capitalize())
print("<--- Cantidad:", cantidad)
print("<--- Total sin descuento: $", total)

if total > 10000:
    descuento = total * 0.20
    total_final = total - descuento
    print("<--- Descuento aplicado: $", descuento)
else:
    total_final = total
    print("<--- No aplica descuento")

#5 - MOSTRAR TOTAL
print("<--- Total a pagar: $", total_final)
print("<----------- GRACIAS POR SU COMPRA ---------->")
print("<------- REALIZADO POR CRISTIAN SOLANO ------>")
print("<---------- GRUPO NUMERO 213022_302 --------->")