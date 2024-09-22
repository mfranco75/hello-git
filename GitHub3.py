def numeros_primos(n):
    """
    Encuentra los números primos entre 1 y n.

    Args:
        n: El límite superior ingresado por el usuario.

    Returns:
        Una lista con los números primos encontrados.
    """

    primos = []
    for num in range(2, n+1):
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

# Pedimos al usuario que ingrese el número
n = int(input("Ingrese un número entero positivo: "))

# Llamamos a la función y mostramos los resultados
resultado = numeros_primos(n)
print("Los números primos hasta", n, "son:", resultado)