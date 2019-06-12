import unittest
import ta_backtest.tools.data_loader as loader


class TestDataLoader(unittest.TestCase):

    def test_from_csv(self):
        with self.assertRaises(FileNotFoundError) as context:
            loader.from_csv('/no_file_is_here')
        self.assertEqual(FileNotFoundError, type(context.exception))

if __name__ == '__main__':
    unittest.main()
