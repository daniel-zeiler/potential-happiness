import unittest

from TakeTwo import Graph as graph_two
import TakeTwo.Graph.Solutions as graph


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

    def test_minimum_vertices_reach_all_nodes(self):
        n = 6
        edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
        output = [0, 3]
        self.assertListEqual(output, graph.minimum_vertices_reach_all_nodes(n, edges))
        n = 5
        edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
        output = [0, 2, 3]
        self.assertListEqual(output, graph.minimum_vertices_reach_all_nodes(n, edges))

    def test_keys_and_rooms(self):
        rooms = [[1], [2], [3], []]
        output = True
        self.assertEqual(output, graph.keys_and_rooms(rooms))
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        output = False
        self.assertEqual(output, graph.keys_and_rooms(rooms))

    def test_number_of_provinces(self):
        isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        output = 2
        self.assertEqual(output, graph.number_of_provinces(isConnected))
        isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        output = 3
        self.assertEqual(output, graph.number_of_provinces(isConnected))
        isConnected = [
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1]
        ]
        output = 1
        self.assertEqual(output, graph.number_of_provinces(isConnected))

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
        self.assertEqual(output, graph_three.possible_bipartition(n, dislikes))
        n = 3
        dislikes = [[1, 2], [1, 3], [2, 3]]
        output = False
        self.assertEqual(output, graph_three.possible_bipartition(n, dislikes))
        n = 5
        dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        output = False
        self.assertEqual(output, graph_three.possible_bipartition(n, dislikes))

    def test_coarse_schedule(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        output = [0, 1]
        self.assertListEqual(output, graph_six.course_schedule_two(numCourses, prerequisites))
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        output = [0, 2, 1, 3]
        self.assertListEqual([0, 1, 2, 3], graph_six.course_schedule_two(numCourses, prerequisites))
        numCourses = 1
        prerequisites = []
        output = [0]
        self.assertListEqual(output, graph_six.course_schedule_two(numCourses, prerequisites))
        numCourses = 2
        prerequisites = [[0, 1]]
        output = [1, 0]
        self.assertListEqual(output, graph_six.course_schedule_two(numCourses, prerequisites))

    def test_calc_equation(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        output = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        self.assertListEqual(output, graph_six.calcEquation(equations, values, queries))
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        output = [3.75000, 0.40000, 5.00000, 0.20000]
        self.assertListEqual(output, graph_six.calcEquation(equations, values, queries))
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        output = [0.50000, 2.00000, -1.00000, -1.00000]
        self.assertListEqual(output, graph_six.calcEquation(equations, values, queries))

    def test_importance(self):
        employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
        input = []
        for employee in employees:
            input.append(graph_six.Employee(employee[0], employee[1], employee[2]))
        id = 1
        output = 11
        self.assertEqual(output, graph_six.getImportance(input, id))
        employees = [[1, 2, [5]], [5, -3, []]]
        input = []
        for employee in employees:
            input.append(graph_six.Employee(employee[0], employee[1], employee[2]))
        id = 5
        output = -3
        self.assertEqual(output, graph_six.getImportance(input, id))

    def test_ladder_length(self):

        word = "hit"
        target = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(5, graph_six.ladderLength(word, target, word_list))

    def test_can_finish(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        output = True
        self.assertEqual(output, graph_six.canFinish(numCourses, prerequisites))
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        output = False
        self.assertEqual(output, graph_six.canFinish(numCourses, prerequisites))
        numCourses = 100
        prerequisites = [[1, 0], [2, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3], [5, 3], [5, 4], [6, 4], [6, 5], [7, 5],
                         [7, 6], [8, 6],
                         [8, 7], [9, 7], [9, 8], [10, 8], [10, 9],
                         [11, 9], [11, 10], [12, 10], [12, 11], [13, 11], [13, 12], [14, 12], [14, 13], [15, 13],
                         [15, 14], [16, 14],
                         [16, 15], [17, 15], [17, 16], [18, 16],
                         [18, 17], [19, 17], [19, 18], [20, 18], [20, 19], [21, 19], [21, 20], [22, 20], [22, 21],
                         [23, 21], [23, 22],
                         [24, 22], [24, 23], [25, 23], [25, 24],
                         [26, 24], [26, 25], [27, 25], [27, 26], [28, 26], [28, 27], [29, 27], [29, 28], [30, 28],
                         [30, 29], [31, 29],
                         [31, 30], [32, 30], [32, 31], [33, 31],
                         [33, 32], [34, 32], [34, 33], [35, 33], [35, 34], [36, 34], [36, 35], [37, 35], [37, 36],
                         [38, 36], [38, 37],
                         [39, 37], [39, 38], [40, 38], [40, 39],
                         [41, 39], [41, 40], [42, 40], [42, 41], [43, 41], [43, 42], [44, 42], [44, 43], [45, 43],
                         [45, 44], [46, 44],
                         [46, 45], [47, 45], [47, 46], [48, 46],
                         [48, 47], [49, 47], [49, 48], [50, 48], [50, 49], [51, 49], [51, 50], [52, 50], [52, 51],
                         [53, 51], [53, 52],
                         [54, 52], [54, 53], [55, 53], [55, 54],
                         [56, 54], [56, 55], [57, 55], [57, 56], [58, 56], [58, 57], [59, 57], [59, 58], [60, 58],
                         [60, 59], [61, 59],
                         [61, 60], [62, 60], [62, 61], [63, 61],
                         [63, 62], [64, 62], [64, 63], [65, 63], [65, 64], [66, 64], [66, 65], [67, 65], [67, 66],
                         [68, 66], [68, 67],
                         [69, 67], [69, 68], [70, 68], [70, 69],
                         [71, 69], [71, 70], [72, 70], [72, 71], [73, 71], [73, 72], [74, 72], [74, 73], [75, 73],
                         [75, 74], [76, 74],
                         [76, 75], [77, 75], [77, 76], [78, 76],
                         [78, 77], [79, 77], [79, 78], [80, 78], [80, 79], [81, 79], [81, 80], [82, 80], [82, 81],
                         [83, 81], [83, 82],
                         [84, 82], [84, 83], [85, 83], [85, 84],
                         [86, 84], [86, 85], [87, 85], [87, 86], [88, 86], [88, 87], [89, 87], [89, 88], [90, 88],
                         [90, 89], [91, 89],
                         [91, 90], [92, 90], [92, 91], [93, 91],
                         [93, 92], [94, 92], [94, 93], [95, 93], [95, 94], [96, 94], [96, 95], [97, 95], [97, 96],
                         [98, 96], [98, 97],
                         [99, 97]
                         ]
        output = True
        self.assertEqual(output, graph_six.canFinish(numCourses, prerequisites))

    def test_maximum_distance_traveled(self):
        edges = [[1, 2, 1], [2, 3, 2], [2, 4, 3], [1, 5, 4]]
        number_of_cities = 5
        self.assertEqual(22, graph_two.maximum_distance_travelled_by_all_couples(number_of_cities, edges))

    def test_number_of_buses(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        source = 1
        target = 6
        output = 2
        self.assertEqual(output, graph_four.numBusesToDestination(routes, source, target))
        routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
        source = 15
        target = 12
        output = -1
        self.assertEqual(output, graph_four.numBusesToDestination(routes, source, target))
        routes = [[2], [2, 8]]
        source = 8
        target = 2
        output = 1
        self.assertEqual(output, graph_four.numBusesToDestination(routes, source, target))

    def test_k_similar(self):
        s1 = "ab"
        s2 = "ba"
        output = 1
        self.assertEqual(output, graph_four.kSimilarity(s1, s2))
        s1 = "abc"
        s2 = "bca"
        output = 2
        self.assertEqual(output, graph_four.kSimilarity(s1, s2))
        s1 = "the"
        s2 = "cat"
        output = -1
        self.assertEqual(output, graph_four.kSimilarity(s1, s2))

    def test_count_paths(self):
        n = 7
        roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                 [0, 4, 5], [4, 6, 2]]
        self.assertEqual(4, graph_six.countPaths(n, roads))
        n = 2
        roads = [[1, 0, 10]]
        self.assertEqual(1, graph_six.countPaths(n, roads))

    def test_find_the_city(self):
        n = 4
        edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
        distanceThreshold = 4
        output = 3
        self.assertEqual(output, graph_six.findTheCity(n, edges, distanceThreshold))

    def test_makeConnections(self):
        n = 4
        connections = [[0, 1], [0, 2], [1, 2]]
        output = 1
        self.assertEqual(output, graph_six.makeConnected(n, connections))
        n = 6
        connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
        output = 2
        self.assertEqual(output, graph_six.makeConnected(n, connections))
        n = 6
        connections = [[0, 1], [0, 2], [0, 3], [1, 2]]
        output = -1
        self.assertEqual(output, graph_six.makeConnected(n, connections))

    def test_max_probability(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.2]
        start = 0
        end = 2
        output = 0.25000
        self.assertEqual(output, graph_six.maxProbability(n, edges, succProb, start, end))
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.3]
        start = 0
        end = 2
        output = 0.3000
        self.assertEqual(output, graph_six.maxProbability(n, edges, succProb, start, end))
        n = 3
        edges = [[0, 1]]
        succProb = [0.5]
        start = 0
        end = 2
        output = 0.0000
        self.assertEqual(output, graph_six.maxProbability(n, edges, succProb, start, end))

    def test_find_cheapest_flights(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        output = 200
        self.assertEqual(output, graph_six.findCheapestPrice(n, flights, src, dst, k))
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        output = 500
        self.assertEqual(output, graph_six.findCheapestPrice(n, flights, src, dst, k))


if __name__ == '__main__':
    unittest.main()
