print("<----------------- PIZZERÍA ---- -------------------->")
print("<----------- SISTEMA DE VENTAS AUTOMATIZADO --------->")

# 1 - BASE DE DATOS BASADA EN ARREGLOS O LISTAS
# Usamos el índice 0 como vacío para que la posición 1 coincida con el Tipo 1

precios = [0, 10000, 15000, 20000, 25000, 35000]
porciones = [0, 2, 4, 6, 8, 12]
nombres = ["", "Pequeña", "Mediana", "Larga", "Familiar", "Extra Familiar"]

# VARIABLES PARA ACUMULAR TOTALES GENERALES
cantidades_por_tipo = [0, 0, 0, 0, 0, 0] # Arreglo para contar cuántas de cada una
valor_total_ventas = 0
total_porciones_vendidas = 0

# 2 - INGRESO DE CLIENTES
while True:
    try:
        numero_clientes = int(input("<--- ¿Cuántos clientes desea atender?: "))
        if numero_clientes > 0: break
        print("<--- [ERROR]: Debe ser al menos 1 cliente.")
    except ValueError:
        print("<--- [ERROR]: Ingrese un número válido.")

# 3 - ESTRUCTURA REPETITIVA PARA CLIENTES
for c in range(1, numero_clientes + 1):
    print(f"\n<---------- ATENDIENDO CLIENTE No. {c} ---------->")
    total_cliente = 0
    porciones_cliente = 0
    
    while True:
        print("\n<--- MENÚ DE PIZZAS --->")
        print("1. Pequeña ($10.000)   2. Mediana ($15.000)   3. Larga ($20.000)")
        print("4. Familiar ($25.000)  5. Extra Familiar ($35.000)")
        
        try:
            tipo = int(input("<--- Elija el tipo de pizza (1-5) o 0 para finalizar orden: "))
            
            if tipo == 0:
                break
            elif 1 <= tipo <= 5:
                # PROCESAMIENTO USANDO LOS ARREGLOS
                total_cliente += precios[tipo]
                porciones_cliente += porciones[tipo]
                
                # ACUMULADORES GLOBALES
                cantidades_por_tipo[tipo] += 1
                valor_total_ventas += precios[tipo]
                total_porciones_vendidas += porciones[tipo]
                
                print(f"  [OK] Añadida: Pizza {nombres[tipo]}")
            else:
                print("<--- [ERROR]: Tipo de pizza no válido.")
        except ValueError:
            print("<--- [ERROR]: Ingrese solo números (1-5).")
            
    print(f"<--- TOTAL ORDEN CLIENTE {c}: ${total_cliente}")
    print(f"<--- TOTAL PORCIONES CLIENTE {c}: {porciones_cliente}")

# 4 - MOSTRAR RESULTADOS FINALES
print("\n<----------------- REPORTE DE CIERRE ---------------->")
print("<--- Cantidad de pizzas vendidas por tipo:")
for i in range(1, 6):
    print(f"<--- Tipo {i} ({nombres[i]}): {cantidades_por_tipo[i]} unidades")

print("<---------------------------------------------------->")
print(f"<--- VALOR TOTAL DE VENTAS: ${valor_total_ventas}")
print(f"<--- TOTAL PORCIONES VENDIDAS: {total_porciones_vendidas}")

# 5 - PIE DE PÁGINA
print("<---------------------------------------------------->")
print("<------- REALIZADO POR CRISTIAN SOLANO ------>")
print("<---------- GRUPO NUMERO 213022_302 --------->")

