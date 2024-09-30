#Actualiza los valores en diccionarios y listas

def cambiar_numero(matriz):
    for i in range(len(matriz)):  
        for j in range(len(matriz[i])):  
            if matriz[i][j] == 3:  
                matriz[i][j] = 6
    return matriz
matriz = [[10, 15, 20], [3, 7, 14]]
nueva_matriz = cambiar_numero(matriz)
print(nueva_matriz)

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
def cambiar_nombre(cantantes, nuevo_nombre):
    cantantes[0]["nombre"] = nuevo_nombre  # Cambiar el nombre del primer cantante
    return cantantes

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

cantantes_modificados = cambiar_nombre(cantantes, "Enrique Martin Morales")
print(cantantes_modificados)

#En ciudades, cambia “Cancún” por “Monterrey”

def cambiar_ciudad(ciudades):
    # Buscar en la lista de ciudades de México y cambiar "Cancún" por "Monterrey"
    if "Cancún" in ciudades["México"]:
        indice = ciudades["México"].index("Cancún")
        ciudades["México"][indice] = "Monterrey"
    return ciudades

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

ciudades_modificadas = cambiar_ciudad(ciudades)
print(ciudades_modificadas)

#En las coordenadas, cambia el valor de “latitud” por 9.9355431

def cambiar_latitud(coordenadas, nueva_latitud):
    coordenadas[0]["latitud"] = nueva_latitud  # Cambiar el valor de la latitud
    return coordenadas

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

coordenadas_modificadas = cambiar_latitud(coordenadas, 9.9355431)
print(coordenadas_modificadas)

#Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:  # Iterar sobre cada diccionario en la lista
        for llave, valor in diccionario.items():  # Iterar sobre cada llave y valor del diccionario
            print(f"{llave}: {valor}")
        print()

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:  # Verificar si la llave existe en el diccionario
            print(diccionario[llave])

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamada a la función para obtener los nombres
iterarDiccionario2("nombre", cantantes)

#4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{clave}: {len(lista)} elementos")
        for valor in lista:
            print(f"- {valor}")
        print()  # Espacio entre secciones para mejor legibilidad

# Ejemplo de uso
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)