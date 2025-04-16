import datetime
import json
import random
import os

FILENAME = "emotions.json"

"""감정 멘트 출력 (색상 포함, 문장은 조용하게)"""
def get_random_message():
    colors = [
        "\033[96m",  # CYAN
        "\033[92m",  # GREEN
        "\033[93m",  # YELLOW
        "\033[95m",  # MAGENTA
        "\033[91m",  # RED
        "\033[94m",  # BLUE
    ]
    messages = [
        "감정이 정상적으로 저장되었습니다.",
        "입력한 데이터가 기록되었습니다.",
        "정상적으로 처리되었습니다.",
        "감정 로그가 반영되었습니다.",
        "요청이 완료되었습니다.",
        "기록이 성공적으로 완료되었습니다.",
    ]
    msg = random.choice(messages)
    color = random.choice(colors)
    return f"{color}{msg}\033[0m"

"""인트로 출력"""
def show_intro():
    print("🧠" * 14)
    print("🧠🧠🧠🧠 감정 기록기 🧠🧠🧠🧠")
    print("🧠" * 14)

"""메뉴 출력"""
def show_menu():
    print("\n--- [감정기록 메뉴] ---")
    print("1. 감정 기록하기")
    print("2. 감정 목록 보기")
    print("3. 감정 통계 보기")
    print("4. 감정 삭제하기")
    print("5. 종료")
    print("------------------------")

"""감정 불러오기"""
def load_emotions():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

"""감정 기록"""
def log_emotion():
    today = datetime.date.today().strftime("%Y-%m-%d")
    emotion = input("감정을 입력하세요 : ").strip()
    if not emotion:
        print("입력되지 않았습니다. 감정 기록을 종료합니다.")
        return
    reason = input("해당 감정의 이유를 입력하세요 : ").strip()
    if not reason:
        reason = "(이유 없음)"

    entry = {
        "date": today,
        "emotion": emotion,
        "reason": reason
    }

    data = load_emotions()
    data.append(entry)

    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(get_random_message())

"""감정 목록 보기"""
def view_emotions():
    data = load_emotions()
    if not data:
        print("기록된 감정이 없습니다.")
        return
    print("\n📒 기록된 감정 목록:")
    for i, entry in enumerate(data, 1):
        print(f"{i}. [{entry['date']}] {entry['emotion']} - {entry['reason']}")

"""감정 통계 보기"""
def show_stats():
    data = load_emotions()
    print(f"{len(data)}개의 감정이 기록되어 있습니다.")

"""감정 삭제"""
def delete_emotion():
    data = load_emotions()
    if not data:
        print("삭제할 감정이 없습니다.")
        return

    print("\n🗑 삭제할 감정을 선택하세요:")
    for i, entry in enumerate(data, 1):
        print(f"{i}. [{entry['date']}] {entry['emotion']} - {entry['reason']}")

    try:
        choice = int(input("삭제할 번호 입력 : ").strip())
        if 1 <= choice <= len(data):
            removed = data.pop(choice - 1)
            with open(FILENAME, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"[{removed['date']}] {removed['emotion']} 항목이 삭제되었습니다.")
        else:
            print("입력한 번호가 유효하지 않습니다.")
    except ValueError:
        print("숫자를 정확히 입력하세요.")

"""EmotionLogger"""
def main():
    show_intro()
    while True:
        show_menu()
        choice = input("선택 (1~5) : ").strip()
        if choice == "1":
            log_emotion()
        elif choice == "2":
            view_emotions()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            delete_emotion()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효하지 않은 입력입니다.")

if __name__ == "__main__":
    main()