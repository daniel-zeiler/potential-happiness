import TakeTwo.Classes.Solutions2 as classes
import unittest


class SolutionsTest(unittest.TestCase):
    def test_file_system(self):
        file_system = classes.FileSystem()
        file_system.add_file('something.txt', 'this is the contents of the file')
        self.assertEqual('this is the contents of the file', file_system.read_file('something.txt'))
        file_system.add_file('something.txt', 'this is the contents of the file')
        file_system.add_directory('a_dir')
        file_system.add_file('a_dir/something_else.txt', 'how now brown cow')
        self.assertEqual('how now brown cow', file_system.read_file('a_dir/something_else.txt'))
        self.assertListEqual(['something_else.txt'], file_system.list_directory('a_dir'))
        self.assertListEqual(['a_dir', 'something.txt'], file_system.list_directory(''))

    def test_auto_complete_system(self):
        words = ["i love you", "island", "iroman", "i love leetcode"]
        times = [5, 3, 2, 2]
        autoCompleteSystem = classes.AutocompleteSystem(words, times)
        input_character = "i"
        output = ["i love you", "island", "i love leetcode"]
        self.assertCountEqual(output, autoCompleteSystem.input_character(input_character))
        input_character = " "
        output = ["i love you", "i love leetcode"]
        self.assertCountEqual(output, autoCompleteSystem.input_character(input_character))
        input_character = "a"
        output = []
        self.assertCountEqual(output, autoCompleteSystem.input_character(input_character))
        input_character = "#"
        output = []
        self.assertCountEqual(output, autoCompleteSystem.input_character(input_character))
        input_character = "i"
        output = ["i love you", "island", "i love leetcode"]
        self.assertCountEqual(output, autoCompleteSystem.input_character(input_character))

    def test_lru_cache(self):
        lru_cache = classes.LRUCache(2)
        lru_cache.add_item("foo", 1)
        self.assertEqual(lru_cache.get_item("foo"), 1)
        lru_cache.add_item("bar", 2)
        lru_cache.add_item("baz", 3)
        lru_cache.add_item("bing", 4)
        self.assertEqual(lru_cache.get_item("foo"), None)


