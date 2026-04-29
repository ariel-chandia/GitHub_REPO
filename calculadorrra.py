print("=== Calculadora ===")
num1 = float(input("ingresa el primer número: "))
num2 = float(input("ingresa el segundo número: "))
operacion = input("¿Qué operación? (suma, resta, multiplica, divide): ")

if operacion == "suma":
    resultado = num1 + num2
elif operacion == "resta":
    resultado = num1 - num2
elif operacion == "multiplica":
    resultado = num1 * num2
elif operacion == "divide":
    resultado = num1 / num2

print("El resultado es:", resultado)