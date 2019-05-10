def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n,visited)
    return visited

graph = {}
num_nodes = int(input("Enter the number of node : "))
nodes = [x for x in input("Enter the nodes : ").split()]
for i in range(num_nodes):
    num_adj_nodes = int(input("Enter the number of nodes adjacent to "+nodes[i]+" : "))
    adj_nodes = [x for x in input("Enter the adjacent nodes : ").split()]
    graph[nodes[i]] = adj_nodes

if len(dfs(graph,nodes[0],[]))!=len(nodes):
    print("Not connected")
else:
    print("Connected")
