def getStartNode(graph,nodes):
    allNodes = []
    for i in graph:
        allNodes+=graph[i]
    candidateStartNode = list(set(nodes)-set(allNodes))
    startnode = candidateStartNode[0]
    return startnode

graph = {
    'a' : ['b'],
    'b' : ['c','d'],
    'c' : ['e'],
    'd' : ['e'],
    'e' : []
}

nodes = ['a','b','c','d','e']

n = len(nodes)
topsort = []
for i in range(n):
    topsort.append(getStartNode(graph,nodes))
    graph.pop(topsort[i])
    nodes.remove(topsort[i])

print(topsort)        
