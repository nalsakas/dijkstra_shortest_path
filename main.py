class Node:
    def __init__(self, name = None, weight = float('inf')):
        self.name = name
        self.weight = weight

def edge_to_adjacency(edges:list):
    adjacency = {}
    for item in edges:
        src, dst, weight = item
        if src not in adjacency:
            adjacency[src] = []
        if dst not in adjacency:
            adjacency[dst] = []

        adjacency[src].append(Node(dst, weight))
        adjacency[dst].append(Node(src, weight))
    
    return adjacency

def dijkstra_shortest_path(src:str, dst:str, edges:list):
    adjacency = edge_to_adjacency(edges)
    visited = set()
    table = {node: Node() for node in adjacency.keys()}
    table[src].weight = 0

    def dfs(src:str, dst:str, adjacency:dict, visited:list, table:dict):
        if src == dst:
            return

        if src in visited:
            return
        
        visited.add(src)
        
        for neighbor in adjacency[src]:
            if table[src].weight + neighbor.weight < table[neighbor.name].weight:
                table[neighbor.name].weight = table[src].weight + neighbor.weight
                table[neighbor.name].name = src
        
        current = Node()
        for neighbor in adjacency[src]:
            if neighbor.name not in visited:
                if table[neighbor.name].weight < current.weight:
                    current = neighbor
        
        dfs(current.name, dst, adjacency, visited, table)
    
        return table
    
    table = dfs(src, dst, adjacency, visited, table)
    
    result = f"{dst}"
    current = dst
    while current:
        current = table[current].name
        if current is not None:
            result = f"{current}," + result
    
    return result



if __name__ == '__main__':
    edges = [
        ['A', 'B', 2],
        ['A', 'D', 8],
        ['B', 'E', 6],
        ['D', 'B', 5],
        ['D', 'E', 3],
        ['D', 'F', 2],
        ['E', 'C', 9],
        ['F', 'E', 1],
        ['F', 'C', 3]
    ]
    shortest_path = dijkstra_shortest_path('A', 'C', edges)
    print(shortest_path)