#!/usr/bin/env python3

def pedirNumero():
    num1 = int(input(f"Introduce un número entero: "))
    try:
        if num1 > 0:
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
            return resta(resultado)

        elif operador == "s":
            return "s"
        else:
            raise ValueError (f"No es un operador válido")
    
    except ValueError as e:
        print(f"[!] Error: ", e)
        return validarOperador()


operador = ""
resultado = None
while operador != "s":

    if resultado is None:
        resultado = pedirNumero()

    operador = validarOperador(resultado)
    if operador != "s":
        resultado = operador

print("Salimos del programa")
print(f"[+] El resultado de las operaciones es {resultado}")
