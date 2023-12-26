import unittest
import game
import maze

class TestGame(unittest.TestCase):

    def test1_example_test(self):
        '''An example test that shows all the steps to initialize and invoke the solution algorithm'''

        # Create the maze grid to whatever size you want. But make it 2x2 or greater.
        grid = maze.Maze(5, 5)
        # Use this method to create test mazes
        grid._set_maze([["*", 1,  "*",  1,  1],
                        [2,   5,  "*", "*", 2],
                        [3,  "*", "*", "*", 8],
                        [9,  "*",  4,   7,  3],
                        [1,   3,   1,  "*", 2] ])
        start = (0,1)
        end = (0,3)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, end)
        # Attach the maze to game instance
        testgame = game.Game(grid)
        # Initiate your recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        # If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        # Each test should assert the correct wining score and the correct winning path
        self.assertEqual(score, 49)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3)])

    #############################################
    # TODO - add the rest of your test cases here
    
        grid = maze.Maze(5, 5)
        grid._set_maze([["*", 1,  "*",  1,  1],
                        [2,   5,  "*", "*", 2],
                        [3,  "*", "*", "*", 8],
                        [9,  "*",  4,   7,  3],
                        [1,   3,   1,  "*", 2] ])
        start = (0,1)
        finish = (1,3)
        grid.set_start_finish(start, finish)
        testgame2 = game.Game(grid)
        score, path = testgame2.find_route(start[0], start[1], 0, list())

        #maze is set up to test if the path jumps to finish before getting more points or prioritizes score
        self.assertEqual(score, 50)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3), (1, 
3)])




        grid = maze.Maze(5, 5)
        grid._set_maze([[2, 1, "*", 1, 1],
                        [2, 5, "*", 4, 2],
                        [3, 2, "*", 5, 8],
                        [9, 2, '*', 7, 3],
                        [1, 3, '*', 9, 2] ])
        start = (0,0)
        finish = (4,4)
        grid.set_start_finish(start, finish)
        testgame2 = game.Game(grid)
        score, path = testgame2.find_route(start[0], start[1], 0, list())
        
        #maze is set up to test if the correct output is given when the maze is unsolvable
        self.assertEqual(score, -1)
        self.assertEqual(path, [])




        grid = maze.Maze(5, 5)
        grid._set_maze([[1, 1, 2, 1, 1],
                        [2, 5, 2, 4, 2],
                        [3, 2, 7, 5, 8],
                        [9, 2, 8, 7, 3],
                        [1, 3, 5, 9, 2] ])
        start = (0,0)
        finish = (2,2)
        grid.set_start_finish(start, finish)
        testgame2 = game.Game(grid)
        score, path = testgame2.find_route(start[0], start[1], 0, list())

        #maze is set up to test if the highest score path is taken when given multiple options for routes
        self.assertEqual(score, 87)
        self.assertEqual(path, [(0, 0),(1, 0),(2, 0),(3, 0),(4, 0),(4, 1),(3, 1),(2, 1),(1, 1),(0, 1),(0, 2),(1, 2),(1, 3),(0, 3),(0, 4),(1, 4),(2, 4),(3, 4),(4, 4),(4, 3),(4, 2),(3, 2),(3, 3),(2, 3),(2, 2)])

if __name__ == '__main__':
    unittest.main()
