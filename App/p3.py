import config as cf
import csv
from ADT import list as lt
from DataStructures import listiterator
from time import process_time 

from Sorting import insertionsort 
from Sorting import selectionsort 
from Sorting import quicksort 
from Sorting import mergesort 
from Sorting import quicksort3way
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

lista = lt.newList('ARRAY_LIST', None)

with open("Data/p3.csv", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        lt.addFirst(lista, row)



t1_start = process_time()

#======================================
# Ordenar personas ascendentemente por (apellido, nombre)
#======================================

# insertionsort.insertionSort(lista, less)
# selectionsort.selectionSort(lista, less)
# quicksort.quickSort(lista, less)
# mergesort.mergesort(lista, less)
# quicksort3way.quickSort3Way(lista, less)

#=======================================
# Grupo 1
#=======================================



#=======================================
# Grupo 2
#=======================================


#=======================================
# Grupo 3
#=======================================


#=======================================
# Grupo 4
#=======================================


#=======================================
# Grupo 5
#=======================================


#=======================================
# Grupo 6
#=======================================



#=========================================

t1_stop = process_time()

# Imprimir resultado
iter = listiterator.newIterator(lista)
while listiterator.hasNext(iter):
    c = listiterator.next(iter)
    print(c["apellido"], ",", c["nombre"])

print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
