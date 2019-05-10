nodes = int(input("Enter the number of nodes : "))
n = nodes
matrix = [[0 for x in range(n)]for y in range(n)]
print("Enter the weighted matrix : ")
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())

print("Size of matrix :",n)
print("The weighted matrix :",matrix)

weight = int(0)
visited_bool = [0 for x in range(n)]
visited_bool[0] = int(1)
print(visited_bool)

for i in range(n):
    for j in range(n):
        if matrix[i][j]!=0:
            low = matrix[i][j]
            jtemp = j
            break
    for j in range(n):
        if matrix[i][j]!=0:
            if matrix[i][j]<low:
                low = matrix[i][j]
                jtemp = j
    if visited_bool[i]==1 and visited_bool[jtemp]==0:
        visited_bool[jtemp]=1
        weight = weight + matrix[i][jtemp]
    if visited_bool[i]==0 and visited_bool[jtemp]==1:
        visited_bool[i]==1
        weight =weight + matrix[i][jtemp]
    print("i :",i,"j :",jtemp)

print("The weight of MST is",weight)
