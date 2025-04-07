import random
import os

filename = "quotes.txt"

"""인트로 출력"""
def show_intro():
    print("💬" * 18)
    print(f"💬💬💬💬 오늘의 명언 출력 💬💬💬💬")
    print("💬" * 18)

"""메뉴 출력"""
def show_menu():
    print("\n[1] 명언 추가")
    print("[2] 명언 목록 보기")
    print("[3] 오늘의 명언 랜덤 출력")
    print("[0] 종료")

"""명언 추가"""
def add_quote():
    quote = input("명언을 입력하세요 : ").strip()
    author = input("누구의 명언인가요? : ").strip()
    full_quote = f"{quote} - {author}"
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(full_quote + '\n')
    print("✅ 명언이 저장되었습니다.")

"""명언 전체 보기"""
def view_quotes():
    if not os.path.exists(filename):
        print("! 저장된 명언이 없습니다.")
        return
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = [line.strip() for line in file if line.strip()]
    if quotes:
        print("\n📚 저장된 명언 목록 :")
        for i, q in enumerate(quotes, 1):
            print(f"{i}. {q}")
    else:
        print("! 저장된 명언이 없습니다.")

"""랜덤 명언 출력"""
def print_random_quote():
    if not os.path.exists(filename):
        print("! 저장된 명언이 없습니다.")
        return
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = [line.strip() for line in file if line.strip()]
    if not quotes:
        print("! 저장된 명언이 없습니다.")
        return

    while True:
        quote = random.choice(quotes)
        print(f"\n💬 오늘의 명언 💬\n{quote}\n")

        while True:
            again = input("다른 명언을 더 볼까요? (Y/n) : ").strip().lower()
            if again in ("y", "n", ""):
                break
            print("! 잘못된 입력입니다. Y 또는 n으로 입력해주세요.")

        if again != "" and again != "y":
            break

"""quote_printer"""
def main():
    show_intro()
    while True:
        show_menu()
        choice = input("선택 >> ").strip()
        if choice == "1":
            add_quote()
        elif choice == "2":
            view_quotes()
        elif choice == "3":
            print_random_quote()
        elif choice == "0":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("! 잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()