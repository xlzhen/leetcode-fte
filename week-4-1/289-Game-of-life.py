class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        size_x, size_y = len(board), len(board[0])
        
        def update_cell(x, y):
            live = 0
            if x > 0:
                # check left
                if board[x-1][y][0] == 1:
                    live += 1
            if x < size_x - 1:
                # check right
                if board[x+1][y] == 1:
                    live += 1
            if y > 0:
                # check up
                if board[x][y-1][0] == 1:
                    live += 1
            if y < size_y - 1:
                # check down
                if board[x][y+1] == 1:
                    live += 1
            if x > 0 and y > 0:
                # check up-left
                if board[x-1][y-1][0] == 1:
                    live += 1
            if x > 0 and y < size_y - 1:
                # check up-right
                if board[x-1][y+1][0] == 1:
                    live += 1
            if x < size_x - 1 and y > 0:
                # check down-left
                if board[x+1][y-1] == 1:
                    live += 1
            if x < size_x - 1 and y < size_y - 1:
                # check down-right
                if board[x+1][y+1] == 1:
                    live += 1
            return (board[x][y], live)
        
        for i in range(size_x):
            for j in range(size_y):
                board[i][j] = update_cell(i, j)
        
        for i in range(size_x):
            for j in range(size_y):
                x, y = board[i][j]
                if x == 0 and y == 3:
                    board[i][j] = 1
                elif x == 1 and (y == 2 or y == 3):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
    
        
        
        
                
