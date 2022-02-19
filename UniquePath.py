class Solution(object):
    def uniquePaths(self, obstacleGrid):
        # create obstacleGrid 2D-matrix and initializing with value 0
        paths = [[0]*len(obstacleGrid[0]) for i in obstacleGrid]

        # initializing the left corner if no obstacle there
        if obstacleGrid[0][0] == 0:
            paths[0][0] = 1

        # initializing first column of the 2D matrix
        for i in range(1, len(obstacleGrid)):
            # If not obstacle
            if obstacleGrid[i][0] == 0:
                paths[i][0] = paths[i-1][0]

        # initializing first row of the 2D matrix
        for j in range(1, len(obstacleGrid[0])):

            # If not obstacle
            if obstacleGrid[0][j] == 0:
                paths[0][j] = paths[0][j-1]

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):

                # If current cell is not obstacle
                if obstacleGrid[i][j] == 0:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]

        # returning the corner value of the matrix
        return paths[-1][-1]


ob1 = Solution()
print(ob1.uniquePaths([[1, 0, 0],
                       [0, 1, 0],
                       [0, 0, 0]]))
