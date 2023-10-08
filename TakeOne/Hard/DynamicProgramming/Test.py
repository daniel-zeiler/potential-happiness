import unittest
import TakeOne.Hard.DynamicProgramming.Solution as dp


class SolutionsTest(unittest.TestCase):

    def test_dungeon_game(self):
        dungeon = [
            [-2, -3, 3],
            [-5, -10, 1],
            [10, 30, -5]
        ]
        output = 7
        self.assertEqual(output, dp.calculateMinimumHP(dungeon))


if __name__ == '__main__':
    unittest.main()
