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
corresponding node in the list of graph nodes.

- BFS/DFS is used for graph traversal to check if the word is present. This is similiar to the application of a topological sorting algorithm

- For the maximum points possible in a single round of the game, an implementation of the knapsack problem's solution using dynamic programming is applied.

How to run:
“cat input.json | python WordSearchGame.py | diff answer.txt -”.