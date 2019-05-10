import random
import time
import matplotlib.pyplot as plt

size = []
timess = []
timebs = []
timems = []
timeqs = []
timeis = []
timehs = []
selarr = []
bubarr = []
merarr = []
quiarr = []
insarr = []
heaarr = []

def selection_sort(array,arr_len):
    for i in range(arr_len-1):
        min_index = i
        for j in range(i+1,arr_len):
            if array[j]<array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index],array[i]

def bubble_sort(array,arr_len):
    for i in range(arr_len):
        for j in range(arr_len-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

def merge_sort(array,arr_len):
    if arr_len>1:
        mid = arr_len//2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left,len(left))
        merge_sort(right,len(right))

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            array[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            array = right[j]
            j+=1
            k+=1

def partition(array,low,high):
    pivot = array[high]
    i = low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[i+1],array[high]
    return (i+1)

def quick_sort(array,low,high):
    if low<high:
        pi = partition(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)

def insertion_sort(array,arr_len):
    for i in range(1,arr_len):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key

def heapify(array,arr_len,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left<arr_len and array[i]<array[left]:
        largest = left
    if right<arr_len and array[largest]<array[right]:
        largest = right
    if largest!=i:
        array[largest],array[i] = array[i],array[largest]
        heapify(array,arr_len,largest)

def heap_sort(array,arr_len):
    for i in range(arr_len,-1,-1):
        heapify(array,arr_len,i)
    for i in range(arr_len-1,0,-1):
        array[i],array[0] = array[0],array[i]
        heapify(array,i,0)

for j in range(20):
    array = []
    size.append(50*j)
    for i in range(size[j]):
        array.append(random.randint(1,50*j))

    selarr,bubarr,merarr,quiarr,insarr,heaarr = array,array,array,array,array,array

    start = time.time()
    selection_sort(selarr,size[j])
    end = time.time()
    timess.append(end-start)

    start = time.time()
    bubble_sort(bubarr,size[j])
    end = time.time()
    timebs.append(end-start)

    start = time.time()
    merge_sort(merarr,size[j])
    end = time.time()
    timems.append(end-start)

    start = time.time()
    quick_sort(quiarr,0,size[j]-1)
    end = time.time()
    timeqs.append(end-start)

    start = time.time()
    insertion_sort(insarr,size[j])
    end = time.time()
    timeis.append(end-start)

    start = time.time()
    heap_sort(heaarr,size[j])
    end = time.time()
    timehs.append(end-start)

plt.plot(size,timess,label="selection")
plt.plot(size,timebs,label="bubble")
plt.plot(size,timems,label="merge")
plt.plot(size,timeqs,label="quick")
plt.plot(size,timeis,label="insertion")
plt.plot(size,timehs,label="heap")
plt.legend()
plt.show()
