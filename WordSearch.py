__author__ = 'liu.xingjie'

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        self.h = len(board)
        self.w = len(board[0])
        for i in range(self.h):
            for j in range(self.w):
                if board[i][j] == word[0]:
                    t, board[i][j] = board[i][j], ' '
                    if self.dfs(board, word, i, j, 1):
                        return True
                    board[i][j] = t
        return False

    def dfs(self, board, word, x, y, p):
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        if (p == len(word)):
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < self.h and 0 <= ny and ny < self.w and board[nx][ny] == word[p]:
                t, board[nx][ny] = board[nx][ny], ' '
                if self.dfs(board, word, nx, ny, p + 1):
                    return True
                board[nx][ny] = t
        return False

