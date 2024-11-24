def cycleInGraph(edges):
    graph = build_graph(edges)
    visited, visiting = set(), set()
    print(graph)
    for node in graph:
        if traverse_node(graph, node, visiting, visited):
            return True
    return False


def traverse_node(graph, node, visiting, visited):
    if node in visited:
        return False
    if node in visiting:
        return True
    visiting.add(node)

    for neighbor in graph[node]:
        if traverse_node(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    return False


def build_graph(edges):
    graph = {}

    for idx, edge in enumerate(edges):
        graph[idx] = edge

    return graph