#WORD SEARCH
#Verifies if word is in Board
#Creates random board, uses neighbors to find WORD
#doesn't have to be in the same directions
import random
class Solution(object):
    def exist(self, board, word):

        def neighbor_cells(i, j, n, m, prohibited):
            neighbors = []
            if i != 0 and (i - 1, j) not in prohibited:
                neighbors.append((i - 1, j))
            if i != n - 1 and (i + 1, j) not in prohibited:
                neighbors.append((i + 1, j))
            if j != 0 and (i, j - 1) not in prohibited:
                neighbors.append((i, j - 1))
            if j != m - 1 and (i, j + 1) not in prohibited:
                neighbors.append((i, j + 1))
            return neighbors

        def find_cell(board, letter, start_i, start_j, n, m):
            j = start_j
            for i in range(start_i, n):
                while j != m:
                    if board[i][j] == letter:
                        return (i, j)
                    j += 1
                j = 0
            return (-1, -1)

        def search(word, i, j, n, m, path=1, visited=None):
            if visited is None:
                visited = set()
            neighbors = neighbor_cells(i, j, n, m, visited)
            if path == len(word):
                return True
            if not neighbors:
                return False
            for neighbor in neighbors:
                if board[neighbor[0]][neighbor[1]] == word[path]:
                    if search(word, neighbor[0], neighbor[1], n, m, path + 1, visited | {(i, j)}):
                        return True
            return False


        if not board:
            return False

        i, j = 0, 0
        n, m = len(board), len(board[0])
        beginnings = []
        while i != -1:
            i, j = find_cell(board, word[0], i, j, n, m)
            beginnings.append((i, j))
            j += 1
        beginnings.pop()

        if len(word) == 1:
            return bool(beginnings)

        for beginning in beginnings:
            if search(word, beginning[0], beginning[1], n, m):
                return True
        return False

class Board(object):
    def __init__(self, x, y):
        self.matrix = []
        self.temp = []
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, index):
        return self.matrix[index]

    def makeBoard(self):
        for i in range(self.y):
            self.temp = []
            for j in range(self.x):
                self.temp.append(self.alphabet[random.randint(0, 25)])
            self.matrix.append(self.temp)

    def printBoard(self):
        for i in self.matrix:
            print(i)

board = Board(5, 5)
board.makeBoard()
board.printBoard()
s = Solution()
x = input('Enter word to verify if it exists in the board:')
print(s.exist(board, x))
