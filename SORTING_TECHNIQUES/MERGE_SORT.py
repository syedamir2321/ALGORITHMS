import matplotlib.pyplot as plt
import random
import time

size = []
timems = []

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
                array[k]=left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            array[k]=right[j]
            j+=1
            k+=1

for j in range(50):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    start = time.time()
    merge_sort(array,size[j])
    end = time.time()

    timems.append(end-start)

plt.plot(size,timems,label="merge sort")
plt.legend()
plt.show()
