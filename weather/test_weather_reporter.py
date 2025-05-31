import unittest
from unittest.mock import Mock
from weather.weather_service import WeatherReporter


class TestWeatherReporter(unittest.TestCase):
    def test_report_temperature(self):
        # Создаем мок для WeatherService
        mock_weather_service = Mock()
        mock_weather_service.get_temperature.return_value = 25

        # Тестируемый объект
        reporter = WeatherReporter(mock_weather_service)
        result = reporter.report_temperature("Almaty")

        # Проверки
        self.assertEqual(result, "Temperature in Almaty is 25°C")
        mock_weather_service.get_temperature.assert_called_once_with("Almaty")


if __name__ == "__main__":
    unittest.main()
