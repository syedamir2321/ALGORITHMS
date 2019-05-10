import matplotlib.pyplot as plt
import time
import random

size = []
timess = []

def selection_sort(array,arr_len):
    for i in range(arr_len-1):
        min_index = i
        for j in range(i+1,arr_len):
            if array[j]<array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index],array[i]

for j in range(20):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    print(array)

    start = time.time()
    selection_sort(array,size[j])
    end = time.time()

    timess.append(end-start)

plt.plot(size,timess,label="selection sort")
plt.legend()
plt.show()    
