import TakeTwo.Classes.Solutions as classes


def test_file_system(self):
    file_system = classes.FileSystem()
    file_system.add_file('/something.txt', 'this is the contents of the file')
    self.assertEqual('this is the contents of the file', file_system.read_file('/something.txt'))
    file_system.add_file('/something.txt', 'this is the contents of the file')
    file_system.add_directory('/a_dir')
    file_system.add_file('/a_dir/something_else.txt', 'how now brown cow')
    self.assertEqual('how now brown cow', file_system.read_file('a_dir/something_else.txt'))
    self.assertListEqual(['something_else.txt'], file_system.list_directory('/a_dir'))
    self.assertListEqual(['a_dir', 'something.txt'], file_system.list_directory(''))
