import random
import time
import matplotlib.pyplot as plt

size = []
timels = []
timebs = []
timeis = []

for j in range(50):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    def linear_search(array,key):
        for i in range(size[j]):
            if key==array[i]:
                print("Found")
                return
    def binary_search(array,key):
        low = 0
        high = size[j]-1
        while low<=high:
            mid = (low+high)//2;
            if key==array[mid]:
                print("Found")
                return
            elif key<array[mid]:
                high = mid-1
            else:
                low = mid+1
    def interpolation_search(array,key):
        low = 0
        high = size[j]-1
        while low<=high and key>=array[low] and key<=array[high]:
            pos = low + int(float((high-low)/(array[high]-array[low]))*(key-array[low]))
            if key==array[pos]:
                print("Found")
                return
            elif key<array[pos]:
                high = pos-1
            else:
                low = pos+1

    start = time.time()
    linear_search(array,random.randint(1,100))
    end = time.time()

    timels.append(end-start)

    start = time.time()
    binary_search(array,random.randint(1,100))
    end = time.time()

    timebs.append(end-start)

    start = time.time()
    interpolation_search(array,random.randint(1,100))
    end = time.time()

    timeis.append(end-start)

plt.plot(size,timels,label="linear search")
plt.plot(size,timebs,label="binary search")
plt.plot(size,timeis,label="interpolation search")
plt.legend()
plt.show()
