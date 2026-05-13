FILAS = 5 
ASIENTOS_POR_FILA = 10 
 
def inicializar_sala(): 
    sala = [[0] * ASIENTOS_POR_FILA for _ in range(FILAS)] 
    return sala 
 
def mostrar_sala(sala): 
    print("\n--- Estado de la Sala ---") 
    for f in range(FILAS): 
        print(f"F{f+1}:", end=" ") 
        for estado in sala[f]: 
            simbolo = "" 
            if estado == 0: 
                simbolo = " D" 
            elif estado == 1: 
                simbolo = " V" 
            elif estado == 2: 
                simbolo = " R" 
            print(simbolo, end="") 
        print() 
 
def validar_asiento(sala, fila, asiento): 
    if fila >= 1 and fila <= 5 and asiento >= 1 and asiento <= 10: 
        return 1 
    else: 
        return 0 
 
def obtener_precio(fila): 
    if fila == 1 or fila == 2: 
        return 8000 
    elif fila == 3 or fila == 4: 
        return 6000 
    elif fila == 5: 
        return 4000 
    return 0  
 
def vender_asiento(sala, fila, asiento): 
    if validar_asiento(sala, fila, asiento) == 0: 
        return 0 
         
    indice_fila = fila - 1 
    indice_asiento = asiento - 1 
     
    if sala[indice_fila][indice_asiento] == 0: 
        sala[indice_fila][indice_asiento] = 1 
        return obtener_precio(fila) 
    else: 
        return 0 
 
def devolver_asiento(sala, fila, asiento): 
    if validar_asiento(sala, fila, asiento) == 0: 
        return 0 
         
    indice_fila = fila - 1 
    indice_asiento = asiento - 1 
    precio_base = obtener_precio(fila) 
 
    if sala[indice_fila][indice_asiento] == 1: 
        sala[indice_fila][indice_asiento] = 2 
        penalidad = precio_base * 0.20 
        return penalidad 
     
    elif sala[indice_fila][indice_asiento] == 2: 
        sala[indice_fila][indice_asiento] = 0 
        reembolso = precio_base * 0.80 
        return reembolso 
         
    else: 
        return 0 
 
def menu_principal(): 
    sala_cine = inicializar_sala() 
    ingreso_total = 0 
    penalidades_cobradas = 0 
    reembolsos_totales = 0 
    opcion = 0 
     
    while opcion != 4: 
        print("\n==============================") 
        print("  Menú: Cine Full") 
        print("================================") 
        print("1. Venta de Asiento.") 
        print("2. Recolección/Devolución de Asiento.") 
        print("3. Mostrar Estado de la Sala.") 
        print("4. Salir.") 
         
        try: 
            opcion = int(input("¿Cuál es su opción? ")) 
        except ValueError: 
            print("Opción no válida.") 
            continue 
             
        if opcion == 1: 
            print("\n--- VENTA DE ENTRADAS ---") 
            try: 
                f = int(input("Ingrese el número de Fila (1-5): ")) 
                a = int(input("Ingrese el número de Asiento (1-10): ")) 
            except ValueError: 
                print("Fila o Asiento deben ser números.") 
                continue 
 
            precio_venta = vender_asiento(sala_cine, f, a) 
             
            if precio_venta != 0:  
                ingreso_total += precio_venta 
                print(f"Venta exitosa. Asiento F{f}-A{a} vendido por ${precio_venta}.") 
            else: 
                print(f"Error en la venta.") 
                 
        elif opcion == 2: 
            print("\n--- RECOLECCIÓN/DEVOLUCIÓN ---") 
            try: 
                f = int(input("Ingrese el número de Fila (1-5): ")) 
                a = int(input("Ingrese el número de Asiento (1-10): ")) 
            except ValueError: 
                print("Fila o Asiento deben ser números.") 
                continue 
                 
            resultado = devolver_asiento(sala_cine, f, a) 
             
            if resultado > 0: 
                if sala_cine[f-1][a-1] == 2: 
                    penalidades_cobradas += resultado 
                    print(f"Devolución solicitada para F{f}-A{a}. Penalidad aplicada: ${resultado}.") 
                else: 
                    reembolsos_totales += resultado 
                    print(f"Devolución completada para F{f}-A{a}. Reembolso: ${resultado}.") 
            else: 
                print(f"El asiento F{f}-A{a} no se puede procesar.") 
                 
        elif opcion == 3: 
            mostrar_sala(sala_cine) 
             
        elif opcion == 4: 
            ingreso_neto = ingreso_total - reembolsos_totales 
            print("\n--- RESUMEN DEL DÍA ---") 
            print(f"Ingresos por Ventas: ${ingreso_total}") 
            print(f"Penalidades Cobradas: ${penalidades_cobradas}") 
            print(f"Reembolsos Realizados: ${reembolsos_totales}") 
            print(f"Ingreso Total Neto: ${ingreso_neto}") 
            print("¡Gracias por usar el sistema!") 
             
        else: 
            print("Opción no reconocida.") 
 
if __name__ == "__main__": 
    menu_principal()