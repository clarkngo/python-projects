graph  = {
  "a" : ["c"],
  "b" : ["c", "e"],
  "c" : ["a", "b", "d", "e"],
  "d" : ["c"],
  "e" : ["c", "b"],
  "f" : []
}

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges

def find_isolated_nodes(graph):
    """return list of isolated nodes"""
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

edges = generate_edges(graph)
iso = find_isolated_nodes(graph)
print(edges)
print(iso)



