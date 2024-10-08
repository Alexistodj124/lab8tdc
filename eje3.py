import time

#Ejercicio 3

n_values = [100000]

#Ejercicio 3

def eje3(n):
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")


execution_times = []

print("Ejercicio 3: ")
for n in n_values:
    start_time = time.time()
    eje3(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append((n, execution_time))


print("\nExecution times:")
for n, exec_time in execution_times:
    print(f"Input Size: {n}, Execution Time: {exec_time:.6f} seconds")