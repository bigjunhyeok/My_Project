import os
from datetime import datetime

"""일기를 저장할 디렉토리 설정"""
JOURNAL_DIR = "journal_directory"

"""설정 정보를 저장할 디렉터리 설정"""
CONFIG_DIR = "config.txt"

"""설정 정보 불러오기"""
def load_config():
    default_config = {
        "author": "",
        "date": datetime.now().strftime("%Y.%m.%d")
    }

    if not os.path.exists(CONFIG_DIR):
        return default_config

    with open(CONFIG_DIR, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            if key in default_config:
                default_config[key] = value.strip()
    return default_config

"""설정 정보 저장하기"""
def save_config(config):
    with open(CONFIG_DIR, "w", encoding="utf-8") as f:
        for key in ("date", "author"):
            f.write(f"{key}={config[key]}\n")

"""인트로 출력"""
def show_intro():
    print("📓" * 20)
    print("📓📓📓📓 데일리 일기 작성기 📓📓📓📓")
    print("📓" * 20)

"""메인 출력"""
def show_main():
    show_intro()
    config = load_config()

    # 날짜 파싱
    try:
        date = datetime.strptime(config.get("date", ""), "%Y.%m.%d")
    except ValueError:
        date = datetime.now()

    author = config.get("author", "")

    print(f"\n🗓  현재 날짜: {date.strftime('%Y.%m.%d')}")
    print(f"✍   작성자: {author or '(미설정)'}")

    # 날짜 변경
    response = input("\n📅 오늘 날짜를 변경할까요? (엔터 = 그대로, Y = 변경): ").strip().lower()
    if response == "y":
        new_date_input = input("변경할 날짜 입력 (예: 2025.04.10): ").strip()
        try:
            date = datetime.strptime(new_date_input, "%Y.%m.%d")
            config["date"] = date.strftime("%Y.%m.%d")
        except ValueError:
            print("⚠ 잘못된 형식입니다. 기존 날짜를 유지합니다.")

    # 작성자 변경
    response = input("\n✏ 작성자를 변경할까요? (엔터 = 그대로, Y = 변경): ").strip().lower()
    if response == "y" or not author:
        new_author = input("새 작성자 이름 입력: ").strip()
        if new_author:
            author = new_author
            config["author"] = author
        else:
            print("⚠ 작성자 입력이 비어 있어 기존 값을 유지합니다.")

    # 설정 저장
    save_config(config)
    return date, author

"""일기 저장 디렉터리가 없으면 생성"""
def ensure_directory():
    if not os.path.exists(JOURNAL_DIR):
        os.makedirs(JOURNAL_DIR)

"""오늘 날짜에 해당하는 파일 이름 생성"""
def get_filename_for_date(date):
    return f"{date.strftime('%Y.%m.%d')}_journal.md"

"""중복을 피해서 저장 가능한 파일 경로를 반환"""
def get_available_filepath(date):
    ensure_directory()
    base_filename = get_filename_for_date(date)
    filepath = os.path.join(JOURNAL_DIR, base_filename)

    if not os.path.exists(filepath):
        return filepath

    # 중복 방지 파일명 처리
    name, ext = os.path.splitext(base_filename)
    counter = 1
    while True:
        new_filename = f"{name} ({counter}){ext}"
        new_filepath = os.path.join(JOURNAL_DIR, new_filename)
        if not os.path.exists(new_filepath):
            return new_filepath
        counter += 1

"""일기 작성"""
def write_entry(date, author):
    filepath = get_available_filepath(date)
    print(f"\n{author}님, 오늘의 일기를 작성하세요.")
    print("✏ 입력 종료는 빈 줄을 두 번 입력하면 됩니다.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            if lines and lines[-1] == "":
                break
        lines.append(line)

    content = "\n".join(lines).strip()
    if not content:
        print("⚠ 내용이 비어 있습니다. 일기 저장을 취소합니다.")
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {date.strftime('%Y년 %m월 %d일 일기')}\n\n")
        f.write(f"- 작성자 : {author}\n\n")
        f.write(content + "\n")

    print(f"\n✅ 일기가 저장되었습니다: {filepath}")

"""DailyJournal"""
def main():
    date, author = show_main()
    write_entry(date, author)

if __name__ == "__main__":
    main()