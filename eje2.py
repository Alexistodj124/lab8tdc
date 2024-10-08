import time

#Ejercicio 2

n_values2 = [1, 10, 100, 1000, 10000, 100000, 1000000]

def eje2(n):
    if n <= 1:
        return
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("Sequence")
            break


execution_times = []

print("Ejercicio 2: ")
for n in n_values2:
    start_time = time.time()
    eje2(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append((n, execution_time))


print("\nExecution times:")
for n, exec_time in execution_times:
    print(f"Input Size: {n}, Execution Time: {exec_time:.6f} seconds")