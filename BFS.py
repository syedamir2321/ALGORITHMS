def bfs(graph,startnode,visited):
    q = [startnode]
    while q:
        v = q.pop(0)
        if not v in visited:
            visited = visited+[v]
            q = q+graph[v]
    return visited

graph = {}
num_nodes = int(input("Enter the number of nodes : "))
nodes = [x for x in input("Enter the nodes : ").split()]
startnode = input("Enter the start node : ")
for i in range(num_nodes):
    num_adj_nodes = int(input("Enter the number of nodes adjacent to "+nodes[i]+" : "))
    adj_nodes = [x for x in input("Enter the adjacent nodes : ").split()]
    graph[nodes[i]] = adj_nodes

print(bfs(graph,startnode,[]))
