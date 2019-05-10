def floyd(graph,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j],(graph[i][k]+graph[k][j]))

graph = []
n = int(input("Enter the number of vertices : "))
print("Enter the weighted adjacency matrix : ")
graph = [[0 for x in range(n)]for y in range(n)]
for i in range(n):
    for j in range(n):
        graph[i][j] = int(input())
        if graph[i][j]==0 and i!=j:
            graph[i][j]=9999

floyd(graph,n)
for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print("")
print("")    
