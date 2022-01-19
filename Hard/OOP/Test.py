import unittest
import Hard.OOP.Solution as oop


class SolutionsTest(unittest.TestCase):

    def test_in_memoery_file_system(self):
        file_system = oop.FileSystem()
        self.assertEqual([], file_system.ls())
        file_system.mkdir("/a/b/c")
        file_system.addContentToFile("/a/b/c/d", "hello")
        self.assertEqual("a", file_system.ls("/"))
        self.assertEqual("hello", file_system.readContentFromFile("/a/b/c/d"))


if __name__ == '__main__':
    unittest.main()
