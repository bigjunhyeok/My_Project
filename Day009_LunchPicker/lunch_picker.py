import os
import random

menu_file = "menu_list.txt"
menu_list = []

"""메뉴 불러오기"""
def load_menu():
    menu_list.clear()  # 중복 방지
    if os.path.exists(menu_file):
        with open(menu_file, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    menu_list.append(clean_line)

"""메뉴 저장하기"""
def save_menu():
    with open(menu_file, "w", encoding="utf-8") as file:
        for menu in menu_list:
            file.write(menu + "\n")

"""인트로 출력"""
def show_intro():
    print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")
    print("🍴🍴🍴🍴점심 메뉴 추천기 🍴🍴🍴🍴")
    print("🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴\n")

    print("1. 기존 메뉴 중에서 추천")
    print("2. 메뉴를 추가하고 추천")
    print("3. 저장된 메뉴 리스트 출력")
    print("4. 저장된 메뉴 리스트 초기화")
    print("5. 특정 메뉴 삭제")
    print("q. 종료\n")

    choice = input("원하는 모드를 선택하세요 (1/2/3/4/5/q) : ").strip()
    return choice

"""기존 메뉴 추천"""
def recommend_existing():
    load_menu()
    if not menu_list:
        print("❌ 저장된 메뉴가 없습니다!")
        print("🔄 메뉴를 추가해야 합니다.\n")
        add_and_recommend()
        return

    print("\n--------------------")
    print("🤔 오늘 점심은...")
    print("👉", random.choice(menu_list))
    print("--------------------")

    while True:
        again = input("\n🎲 다시 추천할까요? (y/n) : ").strip().lower()
        if again == 'y':
            print("\n--------------------")
            print("🤔 오늘 점심은...")
            print("👉", random.choice(menu_list))
            print("--------------------")
            continue
        elif again == 'n':
            print("👋 종료합니다!")
            break
        else:
            print("❌ 잘못된 입력입니다!")

"""메뉴 추가 및 추천"""
def add_and_recommend():
    load_menu()
    print("\n✍️메뉴를 추가하세요. (종료는 'q')\n")
    while True:
        menu = input("추가할 메뉴 : ")
        if menu.lower() == 'q':
            break
        elif menu.strip() == '':
            print("⚠️메뉴를 입력해 주세요.")
        else:
            if menu not in menu_list:
                menu_list.append(menu)
                print(f"✅ '{menu}' 추가 완료.")
            else:
                print(f"⚠️'{menu}' 이미 포함.")

    if menu_list:
        save_menu()
        print("\n--------------------")
        print("\n🤔 오늘 점심은...")
        print("👉", random.choice(menu_list))
        print("\n--------------------")

        while True:
            again = input("\n🎲 다시 추천할까요? (y/n) : ").strip().lower()
            if again == 'y':
                print("\n--------------------")
                print("🤔 오늘 점심은...")
                print("👉", random.choice(menu_list))
                print("--------------------")
            elif again == 'n':
                print("👋 종료합니다!")
                break
            else:
                print("❌ 잘못된 입력입니다!")
    else:
        print("❌ 저장된 메뉴가 없습니다!")
        print("\n--------------------")

"""저장된 메뉴 보기"""
def show_menu():
    load_menu()
    print("\n--------------------")
    print("\n📋 저장된 메뉴 목록 :")
    if menu_list:
        for idx,menu in enumerate(menu_list, start=1):
            print(f"{idx}. {menu}")
    else:
        print("❌ 저장된 메뉴가 없습니다!")
    print("\n--------------------")

"""전체 메뉴 삭제"""
def clear_menu():
    print("\n--------------------")
    confirm = input("⚠️모든 메뉴를 삭제할까요? (y/n) : ").lower()
    if confirm == 'y':
        open(menu_file, "w", encoding="utf-8").close()  # 파일 비우기
        menu_list.clear()
        print("🗑️ 모든 메뉴가 삭제되었습니다!")
    else:
        print("❎ 삭제 취소.\n")
    print("--------------------")

"""특정 메뉴 삭제"""
def delete_menu_item():
    load_menu()
    if not menu_list:
        print("❌ 삭제할 메뉴가 없습니다!")
        return

    print("\n--------------------")
    print("🗑️ 삭제할 메뉴를 선택하세요 :")
    for idx, menu in enumerate(menu_list, start=1):
        print(f"{idx}. {menu}")
    print("0. 취소")
    print("--------------------")

    try:
        choice = int(input("삭제할 메뉴 번호 입력 : "))
        if choice == 0:
            print("❎ 삭제 취소.\n")
        elif 1 <= choice <= len(menu_list):
            removed = menu_list.pop(choice - 1)
            save_menu()
            print(f"✅ '{removed}' 메뉴 삭제.\n")
        else:
            print("❌ 잘못된 입력입니다!")
    except ValueError:
        print("❌ 잘못된 입력입니다!")

"""lunchpicker"""
def main():
    while True:
        choice = show_intro()
        if choice == '1':
            recommend_existing()
            break
        elif choice == '2':
            add_and_recommend()
            break
        elif choice == '3':
            show_menu()
        elif choice == '4':
            clear_menu()
        elif choice == '5':
            delete_menu_item()
        elif choice.lower() == 'q':
            print("👋 종료합니다!")
            break
        else:
            print("❌ 잘못된 입력입니다!")

if __name__ == "__main__":
    main()