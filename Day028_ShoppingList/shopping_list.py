import os
import json

SHOPPING_FILE = "shopping_list.json"

"""인트로 출력"""
def show_intro():
    print("🛒" * 18)
    print("🛒🛒🛒🛒 쇼핑 리스트 출력 🛒🛒🛒🛒")
    print("🛒" * 18)

"""메뉴 출력"""
def show_menu():
    print("\n--- [쇼핑리스트 메뉴] ---")
    print("1. 항목 추가")
    print("2. 항목 삭제")
    print("3. 목록 보기")
    print("4. 통계 보기")
    print("5. 저장 후 종료")
    print("------------------------")

"""기존 쇼핑 리스트 로드"""
def load_list():
    if os.path.exists(SHOPPING_FILE):
        with open(SHOPPING_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

            # 이전 버전 데이터면 자동 변환 (문자열 리스트 -> 딕셔너리 리스트)
            if data and isinstance(data[0], str):
                return [{"name": name, "price": 0} for name in data]

            return data
    return []

"""쇼핑 리스트 저장"""
def save_list(shopping_list):
    with open(SHOPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(shopping_list, f, ensure_ascii=False, indent=4)

"""항목 추가"""
def add_item(shopping_list):
    name = input("추가할 항목 이름 : ").strip()
    price_input = input("가격 입력 (숫자만) : ").strip()

    if not name or not price_input.isdigit():
        print("- 항목 이름 또는 가격 입력이 잘못되었습니다.")
        return

    price = int(price_input)
    shopping_list.append({"name": name, "price": price})
    print(f"- '{name}' ({price}원) 항목이 추가되었습니다.")

"""항목 삭제"""
def remove_item(shopping_list):
    name = input("삭제할 항목 이름 : ").strip()

    for item in shopping_list:
        if item["name"] == name:
            shopping_list.remove(item)
            print(f"- '{name}' 항목이 삭제되었습니다.")
            return

    print("- 해당 항목은 리스트에 없습니다.")

"""현재 쇼핑 리스트 출력 함수"""
def view_list(shopping_list):
    if not shopping_list:
        print("- 쇼핑 리스트가 비어 있습니다.")
    else:
        print("\n📦 현재 쇼핑 리스트:")
        total = 0
        for i, item in enumerate(shopping_list, start=1):
            print(f"  {i}. {item['name']} - {item['price']}원")
            total += item["price"]
        print(f"\n💰 총합: {total}원")

"""통계 출력 함수"""
def show_statistics(shopping_list):
    if not shopping_list:
        print("- 쇼핑 리스트가 비어 있어 통계를 볼 수 없습니다.")
        return

    total_items = len(shopping_list)
    total_price = sum(item["price"] for item in shopping_list)
    average_price = total_price / total_items

    max_item = max(shopping_list, key=lambda x: x["price"])
    min_item = min(shopping_list, key=lambda x: x["price"])

    print("\n📊 쇼핑 리스트 통계")
    print(f"- 총 항목 수 : {total_items}개")
    print(f"- 총합 가격  : {total_price}원")
    print(f"- 평균 가격  : {average_price:.1f}원")
    print(f"- 최고가     : {max_item['name']} ({max_item['price']}원)")
    print(f"- 최저가     : {min_item['name']} ({min_item['price']}원)")

"""ShoppingList"""
def main():
    shopping_list = load_list()
    show_intro()

    while True:
        show_menu()
        choice = input("메뉴 선택 (1-5) : ").strip()

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            show_statistics(shopping_list)
        elif choice == "5":
            save_list(shopping_list)
            print("리스트가 저장되었습니다. 프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()