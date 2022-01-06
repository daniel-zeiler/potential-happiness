import unittest

import output as output

import Graph.Solutions as graph


class SolutionsTest(unittest.TestCase):
    def test_find_town_judge(self):
        n = 2
        trust = [[1, 2]]
        output = 2
        self.assertEqual(output, graph.find_town_judge(n, trust))
        n = 3
        trust = [[1, 3], [2, 3]]
        output = 3
        self.assertEqual(output, graph.find_town_judge(n, trust))
        n = 3
        trust = [[1, 3], [2, 3], [3, 1]]
        output = -1
        self.assertEqual(output, graph.find_town_judge(n, trust))
        n = 3
        trust = [[1, 2], [2, 3]]
        output = -1
        self.assertEqual(output, graph.find_town_judge(n, trust))
        n = 4
        trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
        output = 3
        self.assertEqual(output, graph.find_town_judge(n, trust))

    def test_all_paths_source_to_target(self):
        input = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        output = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        self.assertListEqual(output, graph.all_paths_source_to_target(input))
        input = [[1], []]
        output = [[0, 1]]
        self.assertListEqual(output, graph.all_paths_source_to_target(input))
        input = [[1, 2, 3], [2], [3], []]
        output = [[0, 1, 2, 3], [0, 2, 3], [0, 3]]
        self.assertListEqual(output, graph.all_paths_source_to_target(input))
        input = [[1, 3], [2], [3], []]
        output = [[0, 1, 2, 3], [0, 3]]
        self.assertListEqual(output, graph.all_paths_source_to_target(input))
        input = [[1, 2], [3], [3], []]
        output = [[0, 1, 3], [0, 2, 3]]
        self.assertListEqual(output, graph.all_paths_source_to_target(input))

    def test_keys_and_rooms(self):
        rooms = [[1], [2], [3], []]
        output = True
        self.assertEqual(output, graph.keys_and_rooms(rooms))
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        output = False
        self.assertEqual(output, graph.keys_and_rooms(rooms))

    def test_redundant_connections(self):
        edges = [[1, 2], [1, 3], [2, 3]]
        output = [2, 3]
        self.assertListEqual(output, graph.redundant_connections(edges))
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        output = [1, 4]
        self.assertListEqual(output, graph.redundant_connections(edges))

    def test_maximal_network_rank(self):
        n = 4
        roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
        output = 4
        self.assertEqual(output, graph.maximal_network_rank(n, roads))
        n = 5
        roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
        output = 5
        self.assertEqual(output, graph.maximal_network_rank(n, roads))
        n = 8
        roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        output = 5
        self.assertEqual(output, graph.maximal_network_rank(n, roads))

    def test_find_eventual_safe(self):
        input = [[1, 2], [2, 3], [5], [0], [5], [], []]
        output = [2, 4, 5, 6]
        self.assertListEqual(output, graph.find_eventual_safe_nodes(input))
        input = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
        output = [4]
        self.assertListEqual(output, graph.find_eventual_safe_nodes(input))

    def test_is_graph_bipartite(self):
        input = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        output = False
        self.assertEqual(output, graph.is_graph_bipartite(input))
        input = [[1, 3], [0, 2], [1, 3], [0, 2]]
        output = True
        self.assertEqual(output, graph.is_graph_bipartite(input))

    def test_flower_planting(self):
        n = 3
        paths = [[1, 2], [2, 3], [3, 1]]
        output = [1, 2, 3]
        self.assertListEqual(output, graph.flower_planting_no_adjacent(n, paths))

        n = 4
        paths = [[1, 2], [3, 4]]
        output = [1, 2, 1, 2]
        self.assertListEqual(output, graph.flower_planting_no_adjacent(n, paths))

        n = 4
        paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
        output = [1, 2, 3, 4]
        self.assertListEqual(output, graph.flower_planting_no_adjacent(n, paths))

    def test_network_delay(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        output = 2
        self.assertEqual(output, graph.network_delay_time(times, n, k))
        times = [[1, 2, 1]]
        n = 2
        k = 1
        output = 1
        self.assertEqual(output, graph.network_delay_time(times, n, k))
        times = [[1, 2, 1]]
        n = 2
        k = 2
        output = -1
        self.assertEqual(output, graph.network_delay_time(times, n, k))

    def test_possible_bipartition(self):
        n = 4
        dislikes = [[1, 2], [1, 3], [2, 4]]
        output = True
        self.assertEqual(output, graph.possible_bipartition(n, dislikes))
        n = 3
        dislikes = [[1, 2], [1, 3], [2, 3]]
        output = False
        self.assertEqual(output, graph.possible_bipartition(n, dislikes))
        n = 5
        dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        output = False
        self.assertEqual(output, graph.possible_bipartition(n, dislikes))

    def test_coarse_schedule(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        output = [0, 1]
        self.assertListEqual(output, graph.course_schedule_two(numCourses, prerequisites))
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        output = [0, 2, 1, 3]
        self.assertListEqual(output, graph.course_schedule_two(numCourses, prerequisites))
        numCourses = 1
        prerequisites = []
        output = [0]
        self.assertListEqual(output, graph.course_schedule_two(numCourses, prerequisites))



if __name__ == '__main__':
    unittest.main()
