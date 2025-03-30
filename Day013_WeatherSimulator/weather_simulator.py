import random
from datetime import datetime, timedelta

"""날씨 시뮬레이터 클래스 정의"""
class WeatherSimulator:
    # 처음 객체를 만들 때 자동으로 실행되는 함수 (위치 설정 등 초기화)
    def __init__(self, location="Seoul"):
        self.location = location
        self.weather_types = ["맑음", "흐림", "비", "눈", "바람", "폭풍"]
        self.temperature_range = (-10, 35)
        self.humidity_range = (20, 100)
        self.wind_speed_range = (0, 15)

    # 날짜를 받아서 해당 날의 날씨 정보를 무작위로 생성
    def simulate_weather(self, date: datetime):
        weather = {
            "날짜": date.strftime("%Y-%m-%d"),
            "지역": self.location,
            "날씨": random.choice(self.weather_types),
            "기온(℃)": round(random.uniform(*self.temperature_range), 1),
            "습도(%)": random.randint(*self.humidity_range),
            "풍속(m/s)": round(random.uniform(*self.wind_speed_range), 1)
        }
        return weather

    # 여러 날 동안의 날씨 예보 생성 (기본: 7일)
    def simulate_forecast(self, days=7):
        today = datetime.now()
        forecast = []
        for i in range(days):
            date = today + timedelta(days=i)
            forecast.append(self.simulate_weather(date))
        return forecast

"""보기 좋게 출력"""
def pretty_print(weather_data):
    print(f"📅 {weather_data['날짜']} | 🏙️ 지역: {weather_data['지역']}")
    print(f"☁️ 날씨: {weather_data['날씨']}")
    print(f"🌡️ 기온: {weather_data['기온(℃)']}℃  | 💧 습도: {weather_data['습도(%)']}%  | 🍃 풍속: {weather_data['풍속(m/s)']}m/s")
    print("-" * 50)

if __name__ == "__main__":
    simulator = WeatherSimulator("부산")
    forecast = simulator.simulate_forecast(5)
    for day in forecast:
        pretty_print(day)