def promedio(lista):
    sumatoria = 0
    total = len(lista)
    print(total)
    for x in lista:
        sumatoria = sumatoria + x
    prom = sumatoria / total
    return prom
    
def reprobaron(lista):
    contador = 0
    for x in lista:
        if (x < 6):
            contador = contador + 1
    return contador 
    
def main():
    lista = [8, 9, 10, 6, 6, 7, 8, 9, 5, 6, 7, 6, 8, 8, 9, 9, 5, 6, 7, 9, 10, 7, 8, 9, 9]
    prom = promedio(lista)
    reprobados = reprobaron(lista)
    print("El promedio de los alumnos es de:", prom)
    print("Reprobaron", reprobados, "alumnos")

if __name__ == "__main__":
   main()
