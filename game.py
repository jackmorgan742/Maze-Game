import maze

class Game():
    '''Holds the game solving logic. Initialize with a fully initialized maze'''

    def __init__(self, maze):
        self._maze = maze

    # Creating simple methods (like the next two) to abstract core parts 
    #   of your algorithm helps increase the readability of your code.
    #   You will find these two useful in your solution.

    def _is_move_available(self, row, col, path):
        '''If (row, col) is already in the solved path then it is not available'''
        return (row, col) not in path

    def _is_puzzle_solved(self, row, col):
        '''Is the given row,col the finish square?'''
        return self._maze.get_finish() == (row, col)


    ########################################################
    # TODO - Main recursive method. Add your algorithm here.
    def find_route(self, currow, curcol, curscore, curpath):
        '''
        finds route from start to finish with the best possible score
        '''
        #Checks if current position is invalid or a wall
        if not self._maze.is_move_in_maze(currow, curcol) or self._maze.is_wall(currow, curcol):
            return -1, []

        # Check if current position is the finish
        if self._is_puzzle_solved(currow, curcol):
            return curscore + self._maze.make_move(currow, curcol, curpath), curpath

        #Tests all 4 adjacent positions
        scores = []
        paths = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newrow, newcol = currow + dx, curcol + dy
            if self._is_move_available(newrow, newcol, curpath):
                score, path = self.find_route(newrow, newcol, curscore + self._maze.make_move(currow, curcol, curpath), curpath[:])
                scores.append(score)
                paths.append(path)
                curpath.pop()

        # Return the path with the highest score
        if not scores:
            return -1, []
        best_idx = scores.index(max(scores))
        return scores[best_idx], paths[best_idx]

# This block of code will be useful in debugging your algorithm. But you still need
#  to create unittests to thoroughly testing your code.
if __name__ == '__main__':
    # Here is how you create the maze. Pass the row,col size of the grid.
    grid = maze.Maze(5, 5)
    # You have TWO options for initializing the Value and Walls squares.
    # (1) init_random() and add_random_walls()
    #     * Useful when developing your algorithm without having to create 
    #         different grids
    #     * But not easy to use in testcases because you cannot preditably
    #         know what the winning score and path will be each run
    # (2) _set_maze()
    #     * You have to create the grid manually, but very useful in testing
    #       (Please see the test_game.py file for an example of _set_maze())
    grid._set_maze([    ["*", 1,  "*",  1,  1],
                        [2,   5,  "*", "*", 2],
                        [3,  "*", "*", "*", 8],
                        [9,  "*",  4,   7,  3],
                        [1,   3,   1,  "*", 2] ])
                         
    # AFTER you have used one of the two above methods of initializing 
    #   the Values and Walls, you must set the Start Finish locations. 
    start = (0,1)
    finish = (1,3)
    grid.set_start_finish(start, finish)

    # Printing the starting grid for reference will help you in debugging.
    print(grid)           # Print the maze for visual starting reference

    # Now instatiate your Game algorithm class
    game = Game(grid)     # Pass in the fully initialize maze grid

    # Now initiate your recursize solution to solve the game!
    # Start from the start row, col... zero score and empty winning path
    score, path = game.find_route(start[0], start[1], 0, list())
    print(f"The winning score is {score} with a path of {path}")

