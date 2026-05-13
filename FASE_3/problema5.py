#------------------------------------------------------------
print("<----------------- TIENDA DEPORTIVA ----------------->")
print("<----------- REGISTRO DE HINCHAS FÚTBOL ------------->")
print("<--- ARTÍCULOS: CAMISETA, CHAQUETA, GORRA, MORRAL --->")

# 1 - VARIABLES GLOBALES PARA ACUMULAR DATOS
total_hinchas = 10
asistencia_total = 0
datos_equipos = {} # Diccionario para guardar nombre del equipo y lista de edades
conteo_articulos = {"camiseta": 0, "chaqueta": 0, "gorra": 0, "morral": 0}

# 2 - ESTRUCTURA REPETITIVA (PARA 10 FANÁTICOS)

for i in range(1, total_hinchas + 1):
    print(f"\n<---------- REGISTRO FANÁTICO No. {i} ---------->")
    
    # VALIDACIÓN DEL EQUIPO .strip() quita espacios y .capitalize() asegura que "equipo" y "EQUIPO" sean "Equipo"
    equipo = input("<--- Ingrese su equipo favorito: ").strip().capitalize()

    # VALIDACIÓN DEL ARTÍCULO (Solo permite los 4 definidos)
    while True:
        articulo = input("<--- Artículo preferido (Camiseta/Chaqueta/Gorra/Morral): ").lower().strip()
        if articulo in conteo_articulos:
            conteo_articulos[articulo] += 1
            break
        else:
            print("<--- [ERROR]: Artículo no válido. Intente de nuevo.")

    # VALIDACIÓN DE EDAD (Evita que el programa falle si ingresan letras)
    while True:
        try:
            edad = int(input("<--- Ingrese su edad: "))
            if edad < 0:
                print("<--- [ERROR]: La edad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("<--- [ERROR]: Por favor, ingrese un número entero para la edad.")

    # VALIDACIÓN DE ASISTENCIA
    while True:
        try:
            asistencia = int(input("<--- Días que asiste al estadio al año: "))
            if asistencia < 0:
                print("<--- [ERROR]: Los días no pueden ser negativos.")
                continue
            break
        except ValueError:
            print("<--- [ERROR]: Por favor, ingrese un número para los días.")

    # PROCESAMIENTO DENTRO DEL CICLO
    
    # Acumular asistencia para el promedio general
    asistencia_total += asistencia

    # Organizar edades por equipo
    if equipo not in datos_equipos:
        datos_equipos[equipo] = []
    datos_equipos[equipo].append(edad)


# 3 - MOSTRAR RESULTADOS Y ESTADÍSTICAS

print("\n<----------------- RESUMEN DE DATOS ----------------->")

# A. CANTIDAD Y PROMEDIO DE EDAD POR EQUIPO
print("<--- Estadísticas por Equipo:")
for equipo, edades in datos_equipos.items():
    cantidad = len(edades)
    promedio_edad = sum(edades) / cantidad
    print(f"<--- {equipo}: {cantidad} Hinchas | Edad Promedio: {promedio_edad:.1f}")

# B. ARTÍCULO PREFERIDO
articulo_ganador = max(conteo_articulos, key=conteo_articulos.get)
votos_articulo = conteo_articulos[articulo_ganador]
print("<--- Artículo más pedido:", articulo_ganador.capitalize(), f"({votos_articulo} hinchas)")

# C. PROMEDIO DE ASISTENCIA AL ESTADIO
promedio_asistencia = asistencia_total / total_hinchas
print(f"<--- Promedio de asistencia general: {promedio_asistencia:.1f} días/año")

# 4 - MENSAJE DE DESPEDIDA

print("<---------------------------------------------------->")
print("<---------- REALIZADO POR CRISTIAN SOLANO ----------->")
print("<-------------- GRUPO NUMERO 213022_302 ------------->")