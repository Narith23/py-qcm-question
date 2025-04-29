import unittest


class TestQuizFunctions(unittest.TestCase):

    def test_check_answer_correct(self):
        from main import check_answer
        self.assertTrue(check_answer("ប៉ារីស", "ប៉ារីស"))

    def test_check_answer_wrong(self):
        from main import check_answer
        self.assertFalse(check_answer("លុងដ៍", "ប៉ារីស"))

    def test_calculate_percentage(self):
        from main import calculate_percentage
        self.assertEqual(calculate_percentage(2, 4), 50.0)
        self.assertEqual(calculate_percentage(3, 3), 100.0)

    def test_shuffle_options(self):
        options = ["A", "B", "C", "D"]
        from main import shuffle_options
        shuffled = shuffle_options(options)
        self.assertEqual(set(options), set(shuffled))  # Same items
        self.assertEqual(len(options), len(shuffled))  # Same length


if __name__ == '__main__':
    unittest.main()
