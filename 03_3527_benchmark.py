import AP_03_ordenacao as ap
import random as r
import time as t
import sys as s

s.setrecursionlimit(10000)
r.seed(1001)

def mean_list(n):
    lista = []
    for i in range(n):
        lista.append(r.randint(1,1000))
    return lista

def worst_list(n):
    lista = []
    for i in range(n):
        lista.append(1000 - i)
    return lista

if __name__ == '__main__':
    n_values = [10, 50, 100, 500, 1000, 5000]
    k = 50

    ## 

    print("Algoritmo      ||  N  ||   Cenário   || Tempo Médio")

    for n in n_values:
        time_s = 0
        time_d = 0
        time_q = 0

        for _ in range(k):
            lista = mean_list(n)

            start = t.perf_counter()
            ap.selection_sort(lista)
            end = t.perf_counter()
            time_s += end - start

            start = t.perf_counter()
            ap.divide_and_conquer_sort(lista)
            end = t.perf_counter()
            time_d += end - start

            start = t.perf_counter()
            ap.quick_sort(lista)
            end = t.perf_counter()
            time_q += end - start

        time_s /= k
        time_d /= k
        time_q /= k

        print('-'*60)
        print(f"Selection       || {n} || lista média || {time_s:.10f}s")
        print(f"Div & Conqueror || {n} || lista média || {time_d:.10f}s")
        print(f"Quick Sort      || {n} || lista média || {time_q:.10f}s")

        time_s = 0
        time_d = 0
        time_q = 0

        for _ in range(k):
            lista = worst_list(n)

            start = t.perf_counter()
            ap.selection_sort(lista)
            end = t.perf_counter()
            time_s += end - start

            start = t.perf_counter()
            ap.divide_and_conquer_sort(lista)
            end = t.perf_counter()
            time_d += end - start

            start = t.perf_counter()
            ap.quick_sort(lista)
            end = t.perf_counter()
            time_q += end - start

        time_s /= k
        time_d /= k
        time_q /= k

        print('-'*50)
        print(f"Selection       || {n} || lista média || {time_s:.10f}s")
        print(f"Div & Conqueror || {n} || lista média || {time_d:.10f}s")
        print(f"Quick Sort      || {n} || lista média || {time_q:.10f}s")