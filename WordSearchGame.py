#!/usr/bin/python3.7

# define graph

from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to

    def __init__(self, matrix):
        self.graph = defaultdict(list)
        for i in range(0, len(matrix) - 1):
            for j in range(0, len(matrix[0]) - 1):
                self.addEdge(matrix[i][j], matrix[i + 1][j + 1])
                self.addEdge(matrix[i][j], matrix[i][j + 1])
                self.addEdge(matrix[i][j], matrix[i + 1][j])
                self.addEdge(matrix[i + 1][j + 1], matrix[i][j])
                self.addEdge(matrix[i][j + 1], matrix[i][j])
                self.addEdge(matrix[i + 1][j], matrix[i][j])

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A function used by DFS


    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited[v] = True
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

                # The function to do DFS traversal. It uses

    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

    # take in the JSON file


test_data = {
    "rowCount": 3,
    "columnCount": 3,
    "gameBoard": [
        ["C", "G", "S"],
        ["N", "A", "D"],
        ["I", "Z", "R"]
    ],
    "wordList": [
        "air", "car", "card", "cards",
        "drag", "drags", "sad", "sadden",
        "Sin", "snail", "zig"
    ],
    "letterPoints": {
        "a": 2,
        "e": 2,
        "i": 2,
        "o": 2,
        "u": 2,
        "y": 2
    },
    "wordFindTime": 15,
    "letterIdentifyTime": 2,
    "maxGameTime": 55
}

# sanitize wordFindTime, letterIdentifyTime, maxGameTime


# create list of words to find based on searchability (points + time)


# sanitize word list

# parse JSON word map into adjacency list

# create word search with DFS
matrix = test_data["gameBoard"]
g = Graph(matrix)
print(g.graph)


