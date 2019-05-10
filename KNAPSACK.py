def knapsack(maximum,weight,value,n):
    if n==0 or maximum==0:
        return 0
    if weight[n-1]>maximum:
        return knapsack(maximum,weight,value,n-1)
    else:
        return max(knapsack(maximum,weight,value,n-1),value[n-1]+knapsack(maximum-weight[n-1],weight,value,n-1))

maximum = int(input("Enter the knapsack's capacity : "))
value = [int(x) for x in input("Enter the values : ").split()]
weight = [int(x) for x in input("Enter the weights : ").split()]
n = len(value)
print("The maximum capacity is",knapsack(maximum,weight,value,n))                
