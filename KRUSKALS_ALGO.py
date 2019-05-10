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
source = []
destination = []
edgeweight = []

for i in range(n):
    for j in range(n):
        if i<j and matrix[i][j]!=0:
            edgeweight.append(matrix[i][j])
            source.append(i)
            destination.append(j)

for i in range(len(edgeweight)):
    for j in range(len(edgeweight)-i-1):
        if edgeweight[j]>edgeweight[j+1]:
            edgeweight[j],edgeweight[j+1] = edgeweight[j+1],edgeweight[j]
            source[j],source[j+1] = source[j+1],source[j]
            destination[j],destination[j+1] = destination[j+1],destination[j]

for i in range(len(edgeweight)):
    src = source[i]
    dest = destination[i]
    if visited_bool[src]!=1 or visited_bool[dest]!=1:
        visited_bool[src]=1
        visited_bool[dest]=1
        weight = weight + edgeweight[i]
        print("source :",src+1,"destination :",dest+1)

print("The weight of MST :",weight)
