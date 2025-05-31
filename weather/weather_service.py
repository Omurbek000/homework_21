class WeatherService:
    def get_temperature(self, city):
        # В реальном коде здесь был бы вызов API
        pass


class WeatherReporter:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def report_temperature(self, city):
        temp = self.weather_service.get_temperature(city)
        return f"Temperature in {city} is {temp}°C"
