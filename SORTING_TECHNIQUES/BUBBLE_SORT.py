import random
import matplotlib.pyplot as plt
import time

size = []
timebs = []

def bubble_sort(array,arr_len):
    for i in range(arr_len):
        for j in range(arr_len-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

for j in range(20):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    start = time.time()
    bubble_sort(array,size[j])
    end = time.time()

    timebs.append(end-start)

plt.plot(size,timebs,label="bubble sort")
plt.legend()
plt.show()
