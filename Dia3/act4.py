def promedio(lista):
    cantidad = len(lista)
    sumatoria = 0
    for x in lista:
        sumatoria = sumatoria + lista[x]
    resultado = sumatoria / cantidad
    return resultado
        
def mayor(lista):
    altos = []
    cal_mayor = 0
    for x in lista:
        if(cal_mayor <= lista[x]):
            cal_mayor = lista[x]
    for y in lista:
        if(cal_mayor == lista[y]):
            altos.append(y)
    return cal_mayor, altos
    
def menor(lista):
    bajas = []
    cal_menor = 10
    for x in lista:
        if(cal_menor >= lista[x]):
            cal_menor = lista[x]
    for y in lista:
        if(cal_menor == lista[y]):
            bajas.append(y)
    return cal_menor, bajas

def main():
    lista = {
        "Juan": 8,
        "Giselle": 9,
        "Damian": 5,
        "Ricardo": 6,
        "Yaotzin": 6,
        "Erick": 7,
        "Mario": 8,
        "Edgar": 9,
        "Fernanda": 5,
        "Daniel": 6,
        "Jesus": 7,
        "Damian": 8,
        "Yemahina": 6,
        "Eduardo": 9,
        "Bryan": 9,
        "Mariano": 10,
        "Alberto": 8
    }
    prom = promedio(lista)
    cal_mayor, altas = mayor(lista)
    cal_menor, bajas = menor(lista)
    
    print("El promedio del grupo es de:", prom)
    print("La calificación más alta fue de", cal_mayor, "y la saco: ", altas)
    print("La calificación más baja fue de", cal_menor, "y la saco: ", bajas)

    
if __name__ == "__main__":
   main()