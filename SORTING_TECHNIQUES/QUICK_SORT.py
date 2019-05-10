import random
import time
import matplotlib.pyplot as plt

size = []
timeqs = []

def partition(array,low,high):
    i = low-1
    pivot = array[high]
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[j],array[i] = array[i],array[j]
    array[i+1],array[high] = array[high],array[i+1]
    return (i+1)

def quick_sort(array,low,high):
    if low<high:
        pi = partition(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)
                    
for j in range(50):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    start = time.time()
    quick_sort(array,0,size[j]-1)
    end = time.time()

    timeqs.append(end-start)

plt.plot(size,timeqs,label="quick sort")
plt.legend()
plt.show()
