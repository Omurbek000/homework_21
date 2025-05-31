import unittest
from unittest.mock import patch
from email.sender import notify_user


class TestEmailSender(unittest.TestCase):
    @patch("email.sender.send_email")
    def test_notify_user(self, mock_send_email):
        # Вызываем тестируемую функцию
        notify_user("user@example.com")

        # Проверяем, что send_email вызвана с правильными аргументами
        mock_send_email.assert_called_once_with("user@gmail.com", "Welcome!")


if __name__ == "__main__":
    unittest.main()
