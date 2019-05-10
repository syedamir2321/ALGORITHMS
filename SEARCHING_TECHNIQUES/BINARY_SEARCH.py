import time
import random
import matplotlib.pyplot as plt

size = []
timebs = []

for j in range(50):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    def binary_search(array,key):
        low = 0
        high = size[j]-1
        while low<=high:
            mid = (low+high)//2
            if key==array[mid]:
                print("Found")
                return
            elif key < array[mid]:
                high = mid-1
            else:
                 low = mid+1

    start = time.time()
    binary_search(array,random.randint(1,100))
    end = time.time()

    timebs.append(end-start)

plt.plot(size,timebs,label="binary search")
plt.legend()
plt.show()
