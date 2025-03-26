import random

"""칭찬 리스트"""
compliments_by_category = {
    "1": {  # 에너지 ⚡
        "name": "에너지 넘치는 칭찬 ⚡",
        "items": [
            "오늘도 파이팅이에요!",
            "에너지가 넘치네요!",
            "자신감이 빛나요!",
            "당신의 열정이 멋져요!"
        ]
    },
    "2": {  # 따뜻한 위로 🌷
        "name": "따뜻한 위로 칭찬 🌷",
        "items": [
            "당신은 소중한 사람이에요.",
            "마음이 따뜻해지는 사람이네요.",
            "지금도 충분히 잘하고 있어요.",
            "항상 응원하고 있어요."
        ]
    },
    "3": {  # 창의력 💡
        "name": "창의력 칭찬 💡",
        "items": [
            "당신의 아이디어는 반짝여요!",
            "생각이 정말 창의적이에요.",
            "새로운 걸 보는 눈이 있어요.",
            "참신한 관점이 멋져요!"
        ]
    }
}

"""전체 랜덤 칭찬"""
def get_all_compliments():
    all_items = []
    for category in compliments_by_category.values():
        all_items.extend(category["items"])
    return all_items

"""랜덤 카테고리 칭찬"""
def get_category_compliments(category_choice, name=None):
    if category_choice and category_choice in compliments_by_category:
        items = compliments_by_category[category_choice]["items"]
    else:
        items = get_all_compliments()

    compliment = random.choice(items)
    return f"{name}님, {compliment}" if name else compliment

"""인트로 출력"""
def show_intro():
    print("\n💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯")
    print("💯💯💯💯 랜덤 칭찬 기계 💯💯💯💯")
    print("💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯")

    print("\n📋 메뉴")
    print("1. 전체 랜덤 칭찬")
    print("2. 카테고리 선택 칭찬")
    print("0. 종료")

"""카테고리 출력"""
def show_category():
    print("\n💫 카테고리를 선택하세요:")
    for key, category in compliments_by_category.items():
        print(f"{key}. {category['name']}")

"""재시도 여부 확인"""
# 재시도 여부 확인
def try_agin():
    while True:
        again = input("\n다시 칭찬을 받고 싶으신가요? (y/n) : ").strip().lower()
        if again == 'y':
            break
        elif again == 'n':
            print("😊 다음에 또 만나요!")
            exit()
        else:
            print("⚠️잘못된 입력입니다.")

"""compliment_generator"""
if __name__ == "__main__":
    while True:
        show_intro()
        choice = input("\n메뉴를 선택하세요 : ").strip()

        if choice in ["1", "2"]:
            name_input = input("이름을 입력해주세요 (생략 > Enter) : ").strip()

            while True:
                if choice == "1":
                    # 전체 랜덤 칭찬 선택
                    print("\n💬", get_category_compliments(None, name_input if name_input else None))
                elif choice == "2":
                    # 카테고리 랜덤 칭찬 선택
                    show_category()
                    cat_choice = input("카테고리 번호를 입력하세요 : ").strip()
                    if cat_choice not in compliments_by_category:
                        print("❗ 유효한 카테고리 번호가 아닙니다.")
                        continue
                    print("\n💬", get_category_compliments(cat_choice, name_input if name_input else None))

                if try_agin():
                    continue
                else:
                    break

        elif choice == "0":
            print("😊 다음에 또 만나요!")
            exit()
        else:
            print("⚠️잘못된 입력입니다.")