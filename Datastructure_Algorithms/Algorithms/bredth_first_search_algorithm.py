"""
URL: https://www.youtube.com/watch?v=PQhMkmhYZjQ

"""

from queue import Queue

graph_data = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G", "F"]
}

nodes_visited = {}  # Nodes Visited
node_level = {}  # Distance
parent = {}
bfs_traversal_output = []

queue = Queue()

for node in graph_data.keys():
    nodes_visited[node] = False
    node_level[node] = -1
    parent[node] = None

print(nodes_visited)
print(node_level)
print(parent)

# Define a Source Node
source_node = "A"
nodes_visited[source_node] = True
node_level[source_node] = 0
queue.put(source_node)

while not queue.empty():
    temp_node = queue.get()
    bfs_traversal_output.append(temp_node)
    for adjacent_node in graph_data[temp_node]:
        if not nodes_visited[adjacent_node]:
            nodes_visited[adjacent_node]=True
            parent[adjacent_node]=temp_node
            node_level[adjacent_node] = node_level[temp_node]+1
            queue.put(adjacent_node)

print(nodes_visited)
print(node_level)
print(parent)
print(bfs_traversal_output)


# Distance of node "D" from source node "A"
print(node_level["D"])

# shortest path from the source node
vertex = "G"
shortest_path = []
while vertex is not None:
    shortest_path.append(vertex)
    vertex = parent[vertex]
print(shortest_path[::-1])

