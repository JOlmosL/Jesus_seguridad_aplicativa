def palindromo(palabra):
    palabra_eva = palabra.upper()
    if (palabra_eva == palabra_eva[::-1]):
        print(palabra + " es un palindromo")
    else:
        print(palabra + " no es un palindromo")

def main():
    palabra = str(input("Palabra: "))
    palindromo(palabra)

if __name__ == "__main__":
   main()
