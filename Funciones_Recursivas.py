#Titulo Programa: Funciones Recursivas
#Fecha: 21-Octubre-2022
#Autor: Renteria Arriaga Josue

# Una funcion que se llama asi misma se le conocen funciones recursivas.
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)

        # Funcion que se llama asi misma.
        cuenta_regresiva(numero)
    else:
        print("Hola")
    print(f"Orden de liberacion {numero}")

# Mandamos a llamar a la Funcion.
cuenta_regresiva(10)

# Ejemplo de otra Funcion Recursiva con funcion Hn = (n-1) + Hn-1
def heuristica_pares(numero):
    numero -= 1
    if numero == 0:
        return 0
    else:
        return numero + heuristica_pares(numero)

# Mandamos a llamar a la Funcion y.
numero = heuristica_pares(4)
print(numero)