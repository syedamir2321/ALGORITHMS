def warshall(graph,n):
    R = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = R[i][j] or (R[i][k] and R[k][j])
    for i in R:
        print(i)

graph = []
n = int(input("Enter the number of vertices : "))
print("Enter the adjacency matrix : ")
for i in range(n):
    graph.append([int(x) for x in input().split()])

warshall(graph,n)                        
