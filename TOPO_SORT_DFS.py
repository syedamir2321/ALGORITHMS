def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n,visited)
    return visited

def getStartNode(graph,nodes):
    allNodes = []
    for i in graph:
        allNodes+=graph[i]
    candidateStartNodes = list(set(nodes)-set(allNodes))
    startNode = candidateStartNodes[0]
    return startNode    

graph = {}
num_nodes = int(input("Enter the number of nodes : "))
nodes = [x for x in input("Enter the nodes : ").split()]
for i in range(num_nodes):
    adj_nodes = [x for x in input("Enter the nodes adjacent to "+nodes[i]+" : ").split()]
    graph[nodes[i]] = adj_nodes

startnode = getStartNode(graph,nodes)
print(dfs(graph,startnode,[]))
