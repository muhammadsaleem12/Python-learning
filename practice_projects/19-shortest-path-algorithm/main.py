INF = float("inf")

# The matrix stores connection weights; INF means there is no direct edge.
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]


def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)

    # Start at distance 0; all other nodes are initially unreachable.
    distances = [INF] * n
    distances[start_node] = 0

    # Keep the route to each node and track nodes already processed.
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n

    # Repeatedly select the unvisited node with the smallest known distance.
    for _ in range(n):
        min_distance = INF
        current = -1

        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        # Stop when no unvisited node is reachable.
        if current == -1:
            break

        visited[current] = True

        # Check neighbours and update their distances when a shorter route is found.
        for node_no in range(n):
            distance = matrix[current][node_no]

            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance

                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    # Print one requested route, or every reachable route if no target was given.
    targets = [target_node] if target_node is not None else range(n)

    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue

        # Turn the stored node numbers into a readable path.
        string_path = (str(node) for node in paths[node_no])
        path = " -> ".join(string_path)

        print(
            f"\n{start_node}-{node_no} distance: {distances[node_no]}"
            f"\nPath: {path}"
        )

    return distances, paths


# Find the shortest route from node 0 to node 5.
shortest_path(adj_matrix, 0, 5)
