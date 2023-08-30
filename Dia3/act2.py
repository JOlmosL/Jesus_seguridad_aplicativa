def suma(x, y): return x + y

def resta(x, y): return x - y
    
def multi(x, y): return x * y
    
def div(x, y): return x / y
    
def menu():
    print("Opciones disponibles:")
    print("1 = Sumar\n2 = Restar\n3 = Multiplicar\n4 = Dividir\n0 = Finalizar programa")
    
def main():
    print("Bienvenido a el programa de calculadora")
    opcion = 100
    while(opcion != 0):
        menu()
        opcion = int(input("Opción a elegir: "))
        match opcion:
            case 1:
                valor1 = float(input("Valor 1: "))
                valor2 = float(input("valor 2: "))
                res = suma(valor1, valor2)
                print("Resultado de sumar ", valor1, " + ", valor2, " = ", res)
            case 2:
                valor1 = float(input("Valor 1: "))
                valor2 = float(input("valor 2: "))
                res = resta(valor1, valor2)
                print("Resultado de restar ", valor1, " - ", valor2, " = ", res)
            case 3:
                valor1 = float(input("Valor 1: "))
                valor2 = float(input("valor 2: "))
                res = multi(valor1, valor2)
                print("Resultado de multiplicar ", valor1, " * ", valor2, " = ", res)
            case 4:
                valor1 = float(input("Valor 1: "))
                valor2 = float(input("valor 2: "))
                if(valor2 == 0): 
                    print("No se puede hacer una division entre 0")
                else:
                    res = div(valor1, valor2)
                    print("Resultado de dividir ", valor1, " / ", valor2, " = ", res)
            case 0:
                print("Fin del programa")
    
if __name__ == "__main__":
   main()