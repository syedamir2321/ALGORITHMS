import random
import time
import matplotlib.pyplot as plt

size = []
timehs = []

def heapify(array,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left<n and array[i]<array[left]:
        largest = left
    if right<n and array[largest]<array[right]:
        largest = right
    if largest!=i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array,n,largest)

def heap_sort(array,arr_len):
    for i in range(arr_len,-1,-1):
        heapify(array,arr_len,i)
    for i in range(arr_len-1,0,-1):
        array[i],array[0] = array[0],array[i]
        heapify(array,i,0)

for j in range(50):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    start = time.time()
    heap_sort(array,size[j])
    end = time.time()

    timehs.append(end-start)

plt.plot(size,timehs,label="heap sort")
plt.legend()
plt.show()
