import matplotlib.pyplot as plt
import random
import time

timeis = []
size = []

for j in range(50):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

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
    interpolation_search(array,random.randint(1,100))
    end = time.time()

    timeis.append(end-start)

plt.plot(size,timeis,label="interpolation search")
plt.legend()
plt.show()
