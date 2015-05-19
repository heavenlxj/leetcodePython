__author__ = 'liu.xingjie'

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        g = [[0] * n for i in range(m)]
        #when 1 column, only 1 path
        for i in range(m): g[i][0] = 1
        #when 1 row, only 1 path
        for j in range(n): g[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                g[i][j] = g[i][j-1] + g[i-1][j]
        return g[m-1][n-1]