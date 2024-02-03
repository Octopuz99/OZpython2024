'''
001 args se usa para funciones
- regla: argumentos/parametros, *args, default aprams,  ** kwargs

'''
def suma(valor_uno, valor_dos, valor_tres):
    print(valor_uno + valor_dos + valor_tres)

    #suma (8,8,9)


def suma_calificaciones(*args):
    #los argumentos ls convierte en una tupla
    print(args)
    print(type(args))
    resultado = 0
    for valores in args:
        resultado += valores
    return resultado
#print (suma_calificaciones(8,10,9,6,8,7,9,10))

def promedio_tiempo_vuelta(auto1, auto2):
    promedio = (auto1 + auto2) / 2
    return promedio
#print(promedio_tiempo_vuelta(1.13, 1.35))

def promedio_tiempo_vuelta_optimizada(*args):
    print(args)
    print(len(args))
    print(type(args))
    promedio = 0
    for tiempos in args:
        promedio += tiempos
    return promedio / len(args)
print(promedio_tiempo_vuelta_optimizada (2.20, 2.13,2.13))