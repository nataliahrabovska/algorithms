import unittest

from src.indiana import main


class TestIndiana(unittest.TestCase):

    def test_case_1(self):
        with open('C:/Users/user/PycharmProjects/algo/ijones.in', 'w') as file:
            file.write('3 3\naaa\ncab\ndef\n')
        main()
        with open('C:/Users/user/PycharmProjects/algo/ijones.out', 'r') as file:
            result = int(file.readline().strip())
        self.assertEqual(result, 5)

    def test_case_2(self):
        with open('C:/Users/user/PycharmProjects/algo/ijones.in', 'w') as file:
            file.write('10 1\nabcdefaghi\n')
        main()
        with open('C:/Users/user/PycharmProjects/algo/ijones.out', 'r') as file:
            result = int(file.readline().strip())
        self.assertEqual(result, 2)

    def test_case_3(self):
        with open('C:/Users/user/PycharmProjects/algo/ijones.in', 'w') as file:
            file.write('7 6\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\n')
        main()
        with open('C:/Users/user/PycharmProjects/algo/ijones.out', 'r') as file:
            result = int(file.readline().strip())
        self.assertEqual(result, 201684)


if __name__ == '__main__':
    unittest.main()
