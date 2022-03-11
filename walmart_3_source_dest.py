# question asked in interview of SDE 3 intern @Walmart.
# Given a dictionary of source and destination, return source and destination in list
# Solved with DFS

adj_list = {
    "IND": ["PAK", "RUS"],
    "PAK": ["USA"],
    "USA": ["CHINA"],
    "SRI": ["RUS"],
    "Elite": []
}
color = {}  # mark each node white - "W", Mark Gray while visiting - "G", Black when traversed completely - "B"
parent = {}  # Give parent to each node so that we get idea from which parent we reached this node
dfs_traversal_output = []  # input of source and destination
time = 0
dfs_traversal_time = dict()
for i in adj_list.copy():
    if adj_list[i] == []:
        del adj_list[i]


def dfsUtils(source, u):
    global time
    # if we reached destination
    if len(adj_list[u]) == 0:
        dfs_traversal_output.append([source, u])
    else:
        color[u] = "G"

        time += 1
        # Visit all adjacent nodes
        for v in adj_list[u]:
            if color[v] == "W":
                parent[v] = u
                dfsUtils(source, v)
        color[u] = "B"

        time += 1


sources, destinations = set(), set()

for key, value in adj_list.items():
    destinations.update(value)
    sources.update(key)

# Walmart challenge
dest_values = set()
for val in adj_list.values():
    dest_values.update(val)

# making perfect dict
for i in dest_values:
    if i not in adj_list:
        adj_list[i] = []

for node in adj_list:
    color[node] = "W"
    parent[node] = None

time = 0

for val in adj_list:
    if val not in dest_values:
        dfsUtils(val, val)

print(dfs_traversal_output)
