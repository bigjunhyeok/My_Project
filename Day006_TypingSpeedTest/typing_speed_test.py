import time
import random

"""랜덤 문장 목록"""
sentences = [
    "안녕하세요. 제 이름은 박준혁 입니다.",
    "동해물과 백두산이 마르고 닳도록, 하느님이 보우하사 우리 나라 만세"
]

"""게임 인트로 """
def show_intro():
    print("💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻")
    print("💻💻💻💻 타자 속도 측정 게임 💻💻💻💻")
    print("💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻")
    print("\n랜덤 문장이 출력됩니다. 서둘러 입력하세요!")

"""랜덤 문장을 하나 반환하는 함수"""
def get_random_sentence():
    return random.choice(sentences)

"""정확도 계산"""
def calculate_accuracy(original, typed):
    correct = 0
    for o, t in zip(original, typed):
        if o == t:
            correct += 1
    # 정확도(%) = 맞춘 글자 수 / 전체 글자 수 * 100
    return round((correct / len(original)) * 100, 2)

"""WPM(분당 타자 수) 계산"""
def calculate_wpm(typed_text, elapsed_time):
    words = len(typed_text) / 5  # WPM 기준: 5자 = 1단어
    minutes = elapsed_time / 60
    return round(words / minutes, 2)

"""typing speed test"""
def typing_test():
    show_intro()
    while True:
        input("\n준비되면 Enter 키를 누르세요...")
        test_sentence = get_random_sentence()
        print("\n------------------------------")
        print("\n아래의 문장을 입력하세요!\n")
        print(test_sentence)
        print("\n------------------------------")

        start_time = time.time()
        user_input = input("\n입력: ")
        end_time = time.time()

        elapsed_time = end_time - start_time
        accuracy = calculate_accuracy(test_sentence, user_input)
        wpm = calculate_wpm(user_input, elapsed_time)

        print("\n--- 결과 ---")
        print(f"⏱️ 걸린 시간: {round(elapsed_time, 2)}초")
        print(f"🎯 정확도: {accuracy}%")
        print(f"⌨️ WPM (분당 타자수): {wpm}")

        # 재도전 여부
        retry = input("\n🔄 다시 도전하시겠습니까? (y/n) : ").strip().lower()
        if retry != 'y':
            print("\n👋 게임을 종료합니다.")
            break

if __name__ == "__main__":
    typing_test()