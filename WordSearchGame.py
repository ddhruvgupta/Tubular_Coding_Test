"""
@Author Dhruv Gupta
@Description
This script takes in an input json file which consists of a 2d matrix of charecters, a list of words to search for in the 2d matrix, a 


Input: 
Json File with structure as defined in input.json. input.json is a test file
- wordList: a list of words to search for in the @D char array
- gameBoard: 2D array of chars
- WordfindTime: Time to find first charecter 
- LetterFindTime: Time to find each proceeding charecter

Output: 
Words are present in the 2D matrix of chars. followed by max number of points possible.


Solution:
- Convert each element of 2d array into an object of class node. each node needs the value of the element of the 2d array and the neighbors. 
The neighbors list is represented as a list of indices when the arrary is unrolleded. these index values will then correspond to the the index of the 
corresonding node in the list of graph nodes. 

- BFS/DFS is used for graph traversal to check if the word is present. This is similiar to the application of a topological sorting algorithm 

- For the maximum points possible in a single round of the game, an implementation of the knapsack problem's solution using dynamic programming is applied. 

How to run:
“cat input.json | python WordSearchGame.py | diff answer.txt -”.

"""

import json, sys
from collections import defaultdict


class node:
    """Class represents graph nodes"""
    value = ""
    neighbours = []
    visited = False

    def __init__(self, val):
        """constructor will populate only the value of the node"""
        self.value = val.upper()

    def add(self, n):
        self.neighbours.append(n)

    def visit(self):
        self.visited = True

    def reset(self):
        self.visited = False


def neighbors(a, r, c):
    """neighbors is a list of index of values where the index value is used a a reference to the location in a list of nodes"""
    out = list()
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if 0 <= i < len(a) and 0 <= j < len(a[0]):
                out.append(i * (len(a)) + j)
    out.remove(r * (len(a)) + c)
    return out


def main():
    print("Starting up and accepting json inputs: \n")
    print("usage: cat input.json | python WordSearchGame.py | diff answer.txt -")
    a = sys.stdin
    try:
        inp = json.load(a)
    except ValueError as e:
        print("Input not in json format")
        exit(1)

    gameBoard = inp["gameBoard"]
    wordList = inp["wordList"]


    g = list() # this list is representation of all the nodes of a graph. 
    start = defaultdict(list)

    count = 0
    for i in range(0, len(gameBoard)):
        for j in range(0, len(gameBoard[0])):
            g.append(node(gameBoard[i][j].upper()))
            g[count].neighbours = g[count].neighbours + neighbors(gameBoard, i, j)
            start[gameBoard[i][j]].append(count)
            count += 1


    solution = list()
    for ea in wordList:
        if checkWord(start, g, ea.upper()):
            solution.append(ea)
        reset(g)

    try:
        for ea in solution:
            print(ea, flush=True)

        print(maxScore(solution, inp["letterPoints"], inp["wordFindTime"], inp["letterIdentifyTime"], inp["maxGameTime"]))
        # print(maxScore(solution, letterPoints, 15, 2, 55),flush=True)

    except (BrokenPipeError, IOError):
        print('BrokenPipeError caught', file=sys.stderr)

    sys.stderr.close()


def checkWord(start, g, word):
    """
    Check dictionary of charecter positions to find where the string might start in the graph. 
    If the charecter is found, BFS will start from that point.
    """
    s = start.get(word[0], -1)
    if s == -1:
        return False

    if len(word) == 1 and s != -1:
        return True

    for ea in s:
        soln = BFS(ea, g, word, 1)
        if soln:
            return True
    return False


def BFS(start, g, word, pos):
    """Application of Breath First Search to look for the next best fitting word"""
    if not g[start].visited:
        g[start].visit()
    else:
        return False

    for ea in g[start].neighbours:
        if g[ea].visited:
            continue
        elif g[ea].value == word[pos]:
            if pos == len(word) - 1:
                return True
            else:
                pos += 1
                return BFS(ea, g, word, pos)

    return False


def reset(g):
    for ea in g:
        ea.reset()


def maxScore(solution, letterPoints, wordFindTime, letterIdentifyTime, maxGameTime):
    """Method to find the score of each word based on input points dictionary and time scheme provided in the input"""
    points = list()
    temp = dict()

    temp_points = []
    temp_time = []

    for word in solution:
        p = sum(list(map(lambda x: letterPoints.get(x, 1), word)))
        t = wordFindTime + letterIdentifyTime * (len(word) - 1)
        points.append(p)
        temp.update({word: {"points": p, "time": t}})
        temp_points.append(p)
        temp_time.append(t)

    out = [x for _, x in sorted(zip(points, solution), reverse=True)]

    points_sum = 0
    time_sum = 0


    def knapSack(W, wt, val, n):
        """Knapsack Algorithm application to find the maximum number of points that can be scored in the given configuration"""
        K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
        # Build table K[][] in bottom up manner 
        for i in range(n + 1): 
            for w in range(W + 1): 
                if i == 0 or w == 0: 
                    K[i][w] = 0
                elif wt[i-1] <= w: 
                    K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
                else: 
                    K[i][w] = K[i-1][w] 
        
        return K[n][W]

    maxS = knapSack(maxGameTime,temp_time,temp_points,len(temp_points))
    print(maxS)

if __name__ == '__main__':
    main()