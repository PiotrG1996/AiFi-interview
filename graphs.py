# Numpy provides high performance in memory allocation - it is a good choice for large graphs (written in C)
import numpy as np
import sys

# Show entire matrix in the console
# np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.inf)

# Define the number of vertices and edges
vertices, edges = 10, 10


def generate_graph(vertices, edges):
    """
    Generates a graph with random edges.
    :param vertical: number of vertical edges
    :param horizontal: number of horizontal edges
    :return: a graph
    """
    global graph
    # Create a graph with V vertices and E edges
    graph = np.zeros((vertices, edges), dtype=np.int8)
    # For i = 1 to V
    for i in range(vertices):
        # For j = 1 to E
        for j in range(edges):
            # Create a random number between 0 and 1
            graph[i][j] = np.random.randint(0, 2)
    return graph


def floyd_cycle_finding(graph):
    """
    Find the loop
    :param graph: a graph
    :return: a boolean value indicating whether the graph contains a loop or not
    """
    # Initialize all vertices
    n = graph.shape[0]
    # Create a matrix distance[][] and initialize all
    for k in range(n):
        # Pick all vertices as source one by one
        for i in range(n):
            # Pick all vertices as destination for the above picked source
            for j in range(n):
                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    # Update the value of dist[i][j]
                    graph[i][j] = graph[i][k] + graph[k][j]
    # If we can go from i to j and back to i, then there is a cycle
    for i in range(n):
        # Pick all vertices as source one by one
        if graph[i][i] <= 0:
            return (
                True,
                "Cycle found, total bytes consumed by the elements of the array:",
                graph.nbytes,
            )
    return (
        False,
        "No cycles, total bytes consumed by the elements of the array:",
        graph.nbytes,
    )


# Create test function
if __name__ == "__main__":
    random_array = generate_graph(vertices, edges)
    # print(random_array)
    print(floyd_cycle_finding(random_array))

    # Define an array to test the function
    test_1 = np.array(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    )

    print(floyd_cycle_finding(test_1))

    test_2 = np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )

    print(floyd_cycle_finding(test_2))

    example = np.array(
        [
            [0, 0, 1, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
        ]
    )

    print(floyd_cycle_finding(example))
