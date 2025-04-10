import json
from datetime import datetime

# 생일 정보 저장 파일
DATA_FILE = "birthdays.json"

"""생일 목록을 JSON 파일에서 불러옴"""
def load_birthdays():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

"""생일 목록을 JSON 파일로 저장"""
def save_birthdays(birthdays):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(birthdays, f, ensure_ascii=False, indent=2)

"""사용자로부터 이름과 생일을 입력받아 저장"""
def add_birthday():
    name = input("\n이름을 입력하세요 : ").strip()
    birthday_str = input("생일을 입력하세요 (YYYY.MM.DD) : ").strip()

    try:
        datetime.strptime(birthday_str, "%Y.%m.%d")
    except ValueError:
        print("⚠️날짜 형식이 올바르지 않습니다. 입력을 종료합니다.")
        return

    birthdays = load_birthdays()
    birthdays[name] = birthday_str
    save_birthdays(birthdays)
    print(f"\n✅ {name}의 생일이 저장되었습니다.")

"""저장된 생일 목록을 출력"""
def show_birthdays():
    birthdays = load_birthdays()
    print("\n=== 저장된 생일 목록 ===")
    if not birthdays:
        print("😢 저장된 생일이 없습니다.")
        return
    for name, birthday in birthdays.items():
        print(f"{name} : {birthday}")

"""오늘 날짜와 일치하는 생일을 찾아 출력"""
def check_today_birthdays():
    today = datetime.today().strftime("%m.%d")
    birthdays = load_birthdays()
    found = False

    print(f"\n=== 오늘 생일인 사람 [{today}]===")
    for name, birthday in birthdays.items():
        if birthday[5:] == today:
            print(f"🎉 {name}")
            found = True
    if not found:
        print("😢 오늘 생일인 사람이 없습니다.")

"""인트로 출력"""
def show_intro():
    print("🎉" * 18)
    print("🎉🎉🎉🎉 오늘의 생일 알림 🎉🎉🎉🎉")
    print("🎉" * 18)

"""메인 출력"""
def show_main():
    print("\n--- 생일 알림 리스트 ---")
    print("1. 생일 추가")
    print("2. 저장된 생일 보기")
    print("3. 오늘 생일 확인")
    print("4. 종료")
    print("---------------------")

"""BirthdayReminder"""
def main():
    show_intro()
    while True:
        show_main()
        choice = input("번호를 선택하세요 : ").strip()

        if choice == "1":
            add_birthday()
        elif choice == "2":
            show_birthdays()
        elif choice == "3":
            check_today_birthdays()
        elif choice == "4":
            print("\n👋 프로그램을 종료합니다.")
            break
        else:
            print("\n⚠️올바른 번호를 선택하세요.")

if __name__ == "__main__":
    main()