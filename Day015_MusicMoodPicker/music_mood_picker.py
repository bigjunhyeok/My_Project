import random
import time
import sys
import json

"""플레이리스트 불러오기"""
def load_playlist(file_path="playlist.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

"""인트로 출력"""
def show_intro():
    print("\n🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶")
    print("🎶🎶🎶🎶 Music Mood Picker에 오신 걸 환영합니다! 🎶🎶🎶🎶")
    print("🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶🎶")

"""감정 설정"""
def print_mood_options():
    print("\n당신의 현재 기분이 어떠신가요?")
    for i, mood in enumerate(mood_music.keys(), start=1):
        print(f"{i}. {mood}")

"""로딩 애니메이션"""
def loading_spinner(message="🎶 당신의 기분에 딱 맞는 음악을 찾는 중 🎶", duration=1):
    spinner = ['|', '/', '-', '\\']
    print()  # 한 줄 내려서 깔끔하게 출력
    for _ in range(int(duration / 0.1)):
        for frame in spinner:
            sys.stdout.write(f'\r{message} {frame}')
            sys.stdout.flush()
            time.sleep(0.1)
    print('\r' + ' ' * 80, end='\r')  # 줄 지우기

"""music_mood_picker"""
def pick_music_by_mood():
    print_mood_options()
    while True:
        try:
            choice = int(input("\n번호를 선택하세요 (1~5) : "))
            moods = list(mood_music.keys())
            if 1 <= choice <= len(moods):
                selected_mood = moods[choice - 1]
                loading_spinner()   # 로딩 애니메이션
                song = random.choice(mood_music[selected_mood])
                print(f"🎧 추천 음악 ({selected_mood} 기분): {song}")
                break
            else:
                print("❌ 올바른 번호를 선택해주세요.")
        except ValueError:
            print("❌ 숫자를 입력해주세요.")

if __name__ == "__main__":
    mood_music = load_playlist()
    show_intro()
    pick_music_by_mood()