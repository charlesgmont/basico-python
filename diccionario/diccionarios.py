def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    
    #print(mi_diccionario['llave1'])
    #print(mi_diccionario['llave2'])
    #print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 345667,
        'Brasil': 8737345,
        'Colombia': 78387376,
    }
    #print(poblacion_paises['Brasil'])
    #for pais in poblacion_paises.keys():
        #print(pais)
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes ')


if __name__ == '__main__':
    run()