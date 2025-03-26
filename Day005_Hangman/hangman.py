import time
import random

"""단어장 불러오기"""
def load_words_from_file(filename="words.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]
            if not words:
                print("\n📄 단어장이 비어 있습니다. 단어를 추가하세요.")
                return show_menu()
            return words
    except FileNotFoundError:
        print("\n📄 파일을 찾을 수 없습니다. 단어를 추가하세요.")
        return show_menu()

"""단어 추가"""
def add_word_to_file(filename="words.txt"):
    while True:
        new_word = input("\n➕ 추가할 단어를 입력하세요 : ").strip().lower()

        if not new_word.isalpha():
            print("⚠️알파벳만 입력 가능합니다.")
            continue

        # 파일이 존재하고 마지막 줄이 줄바꿈으로 안 끝나면 개행 추가
        try:
            with open(filename, "rb") as check:
                check.seek(-1, 2)  # 마지막 바이트로 이동
                if check.read() != b'\n':
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("\n")  # 줄바꿈 추가
        except:
            pass  # 파일이 없거나 비어 있을 경우 예외 무시

        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{new_word}\n")
        print(f"✔ '{new_word}'가 추가되었습니다.")
        return show_menu()

"""단어 작성 여부"""
def ask_add_word():
    add_word = input("단어를 추가하시겠습니까? (y/n) : ").strip().lower()
    if add_word in "y":
        add_word_to_file()

"""단어 리스트 조회"""
def show_words_in_file(filename="words.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]
            if not words:
                print("\n📄 단어장이 비어 있습니다. 단어를 추가하세요.")
            print("\n📄 현재 등록된 단어 목록 : ")
            print("🔹 " + "\n🔹 ".join(words))
            return show_menu()
    except FileNotFoundError:
        print("\n📄 파일을 찾을 수 없습니다. 단어를 추가하세요.")
        return show_menu()

"""메뉴 출력"""
def show_main_menu():
    print("🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔")
    print("🤔🤔🤔🤔 행맨 게임 🤔🤔🤔🤔")
    print("🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔")
    time.sleep(0.5)

    # 게임 설명
    hangman_intro = [
        "\n플레이어는 정답을 맞춰야 합니다.",
        "",
        "✅ 게임 규칙 :",
        "1. 컴퓨터가 무작위로 단어를 선택합니다.",
        "2. 플레이어는 알파벳 한 글자를 입력하여 단어를 맞춰야 합니다.",
        "3. 틀릴 때마다 행맨 그림이 점점 완성됩니다.",
        "4. 총 6번 이상 틀리면 게임 종료.",
        ""
    ]
    for line in hangman_intro:
        print(line)
        time.sleep(0.2)
    return show_menu()

"""메뉴 출력"""
def show_menu():
    print("\n############################################################")
    print("🎮 행맨 게임 - 메인 메뉴")
    print("1. 🕹️ 게임 시작")
    print("2. ➕ 단어 추가")
    print("3. 📄 단어장 조회")
    print("4. 👋 게임 종료")
    print("############################################################")

    choice = input("\n원하는 작업을 선택하세요 (1~4) : ").strip()

    if choice == "1":
        play_hangman()
    elif choice == "2":
        add_word_to_file()
    elif choice == "3":
        show_words_in_file()
    elif choice == "4":
        print("프로그램을 종료합니다.")
    else:
        print("⚠️올바른 번호(1~4)를 입력하세요.")

"""행맨의 목숨 단계"""
hangman_stages = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========="""
]

"""hangman"""
def play_hangman():
    words = load_words_from_file()
    word = random.choice(words)
    guessed = []
    tries = 6  # 틀릴 수 있는 최대 횟수
    display = ["_" for _ in word]

    print(hangman_stages[0])
    print("단어:", " ".join(display))

    while tries > 0 and "_" in display:
        guess = input("\n🆎 알파벳을 입력하세요 : ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("한 글자의 알파벳이 아닙니다.")
            continue
        if guess in guessed:
            print("이미 추측했던 알파벳입니다.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"'{guess}'는 이미 포함된 단어입니다.")
            for i, char in enumerate(word):
                if char == guess:
                    display[i] = guess
        else:
            tries -= 1
            print(f"'{guess}' -> 포함되지 않는 단어입니다. 남은 목숨: {tries}")

        print("\n------------------------")
        print(hangman_stages[6 - tries])
        print("단어:", " ".join(display))
        print("입력:", ", ".join(guessed))
        print("\n------------------------")

    # 결과
    if "_" not in display:
        print(f"\n🔥 당신의 승리입니다.\n정답 : {word}")
    else:
        print(f"\n💥 당신의 패배입니다.\n정답 : {word}")

    # 재시작 여부 확인
    while True:
        again = input("\n게임을 다시 시작하시겠습니까? (y/n) : ").strip().lower()
        if again == "y":
            play_hangman()  # 재시작
            break
        elif again == "n":
            show_menu() # 메뉴로 복귀
            break
        else:
            print("⚠️올바른 값을 입력해주세요.")

if __name__ == "__main__":
    show_main_menu()