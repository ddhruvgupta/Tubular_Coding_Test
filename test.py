import json, sys
from collections import defaultdict


class node:
    value = ""
    neighbours = []
    visited = False

    def __init__(self, val):
        self.value = val.upper()

    def add(self, n):
        self.neighbours.append(n)

    def visit(self):
        self.visited = True

    def reset(self):
        self.visited = False


def neighbors(a, r, c):
    out = list()
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if 0 <= i < len(a) and 0 <= j < len(a[0]):
                out.append(i * (len(a)) + j)
    out.remove(r * (len(a)) + c)
    return out


def main():
    a = sys.stdin
    inp = json.load(a)

    # gameBoard = [
    #	 ["C", "G", "C"],
    #	 ["N", "I", "D"],
    #	 ["A", "Z", "N"]
    # ]

    gameBoard = inp["gameBoard"]
    wordList = inp["wordList"]

    g = list()
    start = defaultdict(list)

    count = 0
    for i in range(0, len(gameBoard)):
        for j in range(0, len(gameBoard[0])):
            g.append(node(gameBoard[i][j]))
            g[count].neighbours = g[count].neighbours + neighbors(gameBoard, i, j)
            start[gameBoard[i][j]].append(count)
            count += 1

    # found = checkWord(start, g, "RAG")
    # print(checkWord(start, g, "NID"))
    # reset(g)
    # print(checkWord(start, g, "CNAZAN"))

    solution = list()
    for ea in wordList:
        if checkWord(start, g, ea.upper()):
            solution.append(ea)
        reset(g)

    try:
        for ea in solution:
            print(ea, flush=True)

        print(
            maxScore(solution, inp["letterPoints"], inp["wordFindTime"], inp["letterIdentifyTime"], inp["maxGameTime"]),
            flush=True)

    except (BrokenPipeError, IOError):
        print('BrokenPipeError caught', file=sys.stderr)

    sys.stderr.close()


def checkWord(start, g, word):
    s = start.get(word[0], -1)
    if s == -1:
        return False

    if len(word) == 1 and s != -1:
        return True

    for ea in s:
        soln = DFS(ea, g, word, 1)
        if soln:
            return True
    return False


def DFS(start, g, word, pos):
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
                return DFS(ea, g, word, pos)

    return False


def reset(g):
    for ea in g:
        ea.reset()


def maxScore(solution, letterPoints, wordFindTime, letterIdentifyTime, maxGameTime):
    points = list()
    temp = dict()

    for word in solution:
        p = sum(list(map(lambda x: letterPoints.get(x, 1), word)))
        t = wordFindTime + letterIdentifyTime * (len(word) - 1)
        points.append(p)
        temp.update({word: {"points": p, "time": t}})

    out = [x for _, x in sorted(zip(points, solution), reverse=True)]

    points_sum = 0
    time_sum = 0

    # print(out)

    for word in out:
        t = temp[word]["time"]
        time_sum = time_sum + t
        if time_sum <= maxGameTime:
            points_sum = points_sum + temp[word]["points"]
        else:
            return points_sum


if __name__ == '__main__':
    main()