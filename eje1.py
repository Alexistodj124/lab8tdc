import time

# Tamaños de input
n_values = [1, 10, 100, 1000, 10000]

#Ejercicio 1

def eje1(n):
    counter = 0
    for i in range(n // 2, n + 1):               # Bucle 1
        for j in range(1, n - n // 2 + 1):       # Bucle 2
            k = 1
            while k <= n:                        # Bucle 3
                counter += 1
                k *= 2
print("Ejercicio 1: ")
for n in n_values:
    start_time = time.time()    # Registrar el tiempo antes de la ejecución
    eje1(n)
    end_time = time.time()      # Registrar el tiempo después de la ejecución
    print(f"Input Size: {n}, Execution Time: {end_time - start_time:.6f} seconds")