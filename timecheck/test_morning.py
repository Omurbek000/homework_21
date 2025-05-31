import unittest
from unittest.mock import patch
from timecheck.morning import is_it_morning


class TestMorningCheck(unittest.TestCase):
    @patch("timecheck.morning.datetime")
    def test_is_morning_true(self, mock_datetime):
        # Мокируем datetime.now().hour = 9 (утро)
        mock_datetime.now.return_value.hour = 9
        self.assertTrue(is_it_morning())

    @patch("timecheck.morning.datetime")
    def test_is_morning_false(self, mock_datetime):
        # Мокируем datetime.now().hour = 20 (вечер)
        mock_datetime.now.return_value.hour = 20
        self.assertFalse(is_it_morning())


if __name__ == "__main__":
    unittest.main()
