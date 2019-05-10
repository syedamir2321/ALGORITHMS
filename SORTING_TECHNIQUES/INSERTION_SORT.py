import random
import time
import matplotlib.pyplot as plt

size = []
timeis = []

def insertion_sort(array,arr_len):
    for i in range(1,arr_len):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1]=key
            
for j in range(50):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    start = time.time()
    insertion_sort(array,size[j])
    end = time.time()

    timeis.append(end-start)

plt.plot(size,timeis,label="insertion sort")
plt.legend()
plt.show()
