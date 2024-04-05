#!/usr/bin/env python3

def pedirNumero():
    num1 = int(input(f"Introduce un número entero: "))
    try:
        if num1 > 0:
            lista_numeros.append(num1)
            return num1
        else:
            raise ValueError (f"{num1} no es un número válido, introduce un número entero")
            
    except ValueError as e:
        print(f"[!] Error: ", e)
        return pedirNumero()

def suma(num1):
    num2 = pedirNumero()
    return num1 + num2

def resta(num1):
    num2 = pedirNumero()
    return num1 - num2

def multiplicacion(num1):
    num2 = pedirNumero()
    return num1 * num2

def division(num1):
    num2 = pedirNumero()
    try:
        if num2 == 0:
            raise ZeroDivisionError ("No se puede dividir entre 0")
    except ZeroDivisionError as e0:
        print(f"[!] Error: ", e0)
        return division(num1)

    return num1 / num2
    
def resultadoPrint(resultado, lista_numeros, lista_operadores):
    print(f"[+] El registro de las operaciones es ", end = " ")
    
    for numero, operador in zip(lista_numeros, lista_operadores):
        print(numero, operador, end = " ")
        
    print(lista_numeros[-1], end = " ")  # Imprimir el último número
    print(f"=", resultado)


def validarOperador(resultado):
    operador = input(f"Introduce una operación (+ - * /, s = salir): ")
    try:
        if operador == "+":
            return suma(resultado)

        elif operador == "-":
            return resta(resultado)

        elif operador == "*":
            return multiplicacion(resultado)

        elif operador == "/":
            return division(resultado)
            
        elif operador == "=":
            return resultadoPrint(resultado, lista_numeros, lista_operadores)

        elif operador == "s":
            return "s"
        else:
            raise ValueError (f"No es un operador válido")
    
    except ValueError as e:
        print(f"[!] Error: ", e)
        return validarOperador()
        
    finally:
        if operador != "s" and operador != "=": # Añado los operadores a la lista si sigo realizando operaciones
            lista_operadores.append(operador)

        elif operador == "=": # Vacío las listas al usar "="
            lista_numeros.clear()
            lista_operadores.clear()

        else:
            print("traza finally")

# Declaración de variables
lista_numeros = []
lista_operadores = []
operador = ""
resultado = None

while operador != "s":

    if resultado is None:
        resultado = pedirNumero()

    operador = validarOperador(resultado)
    if operador != "s":
        resultado = operador

resultadoPrint(resultado, lista_numeros, lista_operadores)
print(lista_operadores)
print(lista_numeros)
print("Salimos del programa")
print("Traza de la lista de números", lista_numeros)
print("Traza de la lista de operadores", lista_operadores)

# Añadir al bloque finally un condicional para clear las listas y arrglar lo que ya hay
