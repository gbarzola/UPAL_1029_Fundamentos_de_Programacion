import timeit

tiempo_inicio = timeit.timeit()
print("Tiempo en sec", tiempo_inicio)

print("Proceso...")

tiempo_fin = timeit.timeit()
print("Tiempo en sec", tiempo_fin)

print("Duración", tiempo_fin - tiempo_inicio)
