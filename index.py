print("hola mundo")

# 1. Verificar si un número es par o impar
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Impar")

# 2. Determinar si un número es positivo o negativo
numero = int(input("Ingresa un número: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")

# 3. Comprobar si una persona es mayor o menor de edad
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# 4. Evaluar si un estudiante aprueba una materia
calificacion = int(input("Ingresa tu calificación: "))
if calificacion >= 60:
    print("Aprobado")
else:
    print("Reprobado")

# 5. Clasificar una calificación en letras
calificacion = int(input("Ingresa tu calificación: "))
if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")

# 6. Determinar el estado del agua según la temperatura
temperatura = float(input("Ingresa la temperatura en °C: "))
if temperatura < 0:
    print("Sólido")
elif temperatura <= 100:
    print("Líquido")
else:
    print("Vapor")
