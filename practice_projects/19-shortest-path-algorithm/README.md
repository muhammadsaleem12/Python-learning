# 🧭 Shortest Path Algorithm

A Python implementation of **Dijkstra's shortest path algorithm**. It uses a weighted graph represented by an adjacency matrix to find the shortest distance and route from a starting node to a destination.

## What does it do?

Each number in the adjacency matrix represents the cost of travelling directly between two nodes. `INF` means there is no direct connection.

The example finds the shortest route from **node 0 to node 5**.

## Example result

```text
0-5 distance: 6
Path: 0 -> 2 -> 1 -> 5
```

## Run the project

1. Make sure Python 3 is installed.
2. Open a terminal in this folder.
3. Run:

   ```bash
   python main.py
   ```

## How Dijkstra's algorithm works

1. Set the starting node's distance to `0`; set all other distances to infinity.
2. Select the unvisited node with the smallest known distance.
3. Check its neighbours and update any distance when a shorter route is found.
4. Mark the selected node as visited.
5. Repeat until all reachable nodes have been processed.

The program stores the actual route to each node as well as its distance.

## Concepts practiced

- Graphs and adjacency matrices
- Weighted edges and infinity
- Nested lists and loops
- Tracking visited nodes
- Comparing and updating distances
- Reconstructing paths
- Dijkstra's greedy algorithm

## Important note

Dijkstra's algorithm works with **non-negative edge weights**. It is not suitable for graphs containing negative-weight edges.

---

*Python learning project — Shortest Path Algorithm.*
