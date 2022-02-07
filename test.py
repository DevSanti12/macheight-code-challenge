import requests


# Método que recibe los valores json y la entrada.
def metodoon(data, suma_alturas):
    arr_pos = [] # Esta lista guarda la posición donde va a buscar posteriormente que jugadores encontró.
    hashTable = {} # Este diccionario es la tabla de valores que guarda los valores existentes recorridos para luego se evaluados en la resta
    coincidencia = 0 # Flag coincidencia encontrada.

    # El siguiente for realiza la resta del valor encontrado en la lista values especificamente en h_in para luego hacer una evaluación si el 
    # valor producto de la resta entre la suma de alturas y el valor de h_in se encuentra en hash table para identificar una pareja.

    for i in range(len(data)):
        complement = suma_alturas - int(data[i]['h_in'])
        if complement in hashTable:
            print("Jugadores que suman altura a", suma_alturas,"son: (",(data[i]['first_name']),(data[i]['last_name']),int(data[i]['h_in']),")")
            coincidencia = 1
            arr_pos.append(i)
        hashTable [int(data[i]['h_in'])] = int(data[i]['h_in'])

    return arr_pos,coincidencia


# Método que recibe la entrada.
def peticion(entrada):

    url = "https://mach-eight.uc.r.appspot.com/"

    respuesta = requests.get(url=url)
    data1 = respuesta.json() #se almacena la informacion general en una variable
    data = data1['values'] # se extrae solo los datos dentro de la lista value para poder acceder a las alutras y los nombres 
    
    p,c = metodoon(data, entrada) # se pasan data por parametro a la funcion junto con el valor ingresado por el usuario
    
    if c == False:
        print("no se encontraron coincidencias")


# Método que inicializador
def main():
     while True: 
        try:
            entrada = int(input("Ingresa un valor númerico: ")) # Variable que almae 
        except ValueError:
            print("ERROR ESO NO ES UN ENTERO, INGRESA UN NUMERO ENTERO")
            continue
        else:
            http = peticion(entrada)
            break
    

# Main del proyecto.
if __name__ == "__main__":
    main()