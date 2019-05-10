import random
import matplotlib.pyplot as plt
import time

size = []
timels = []

for j in range(25):
    array = []
    size.append(100*j)
    for i in range(size[j]):
        array.append(random.randint(1,100*j))

    def linear_search(array,key):
        for i in range(size[j]):
            if key==array[i]:
                print("Found")
                return
    start = time.time()
    linear_search(array,random.randint(1,100))
    end = time.time()
    timels.append(end-start)

plt.plot(size,timels,label="linear search")
plt.legend()
plt.show()
