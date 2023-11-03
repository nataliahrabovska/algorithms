import unittest
from src.task_lab4 import add_edge, is_cyclic_disconnected


class TestIsCyclic(unittest.TestCase):
    def test_is_cyclic_disconnected(self):
        adjacency_list = [[] for i in range(5)]
        add_edge(adjacency_list, 0, 1)
        add_edge(adjacency_list, 1, 2)
        add_edge(adjacency_list, 2, 0)
        self.assertTrue(is_cyclic_disconnected(adjacency_list, 5))

    def test_is_not_cyclic_disconnected(self):
        adjacency_list = [[] for i in range(5)]
        add_edge(adjacency_list, 0, 1)
        add_edge(adjacency_list, 2, 3)
        self.assertFalse(is_cyclic_disconnected(adjacency_list, 5))


if __name__ == '__main__':
    unittest.main()
