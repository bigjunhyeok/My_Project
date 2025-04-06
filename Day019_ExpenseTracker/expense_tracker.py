import os

"""인트로 출력"""
def show_intro():
    print("🧾" * 15)
    print("🧾🧾🧾🧾 가계부 프로그램 🧾🧾🧾🧾")
    print("🧾" * 15)

"""프로그램 종료 요청"""
def check_exit(value):
    if value.lower() == 'q':
        print("가계부 종료.")
        exit()

"""금액 입력 유효성 검사"""
def check_amount(prompt):
    while True:
        try:
            value = input(prompt)
            check_exit(value)
            return float(value)
        except ValueError:
            print("올바르지 않은 금액입니다.")

"""수입/지출 구분 입력"""
def check_type():
    # '수입' 또는 '지출' 중 유효한 항목이 입력될 때까지 반복
    while True:
        entry_type = input("항목 유형을 입력하세요 (수입/지출) : ")
        check_exit(entry_type)
        if entry_type in ('수입', '지출'):
            return entry_type
        print("올바른 항목 유형을 입력하세요. (수입 또는 지출)")

"""가계부 항목 추가"""
def add_entry(expenses):
    print("\n[항목 추가]")
    entry_type = check_type()
    description = input("설명을 입력하세요 : ")
    check_exit(description)
    amount = check_amount("금액을 입력하세요 : ")

    # 항목을 딕셔너리로 구성 후 리스트에 추가
    expenses.append({
        '유형' : entry_type,
        '설명' : description,
        '금액' : amount
    })
    print("항목이 추가되었습니다.\n")

"""전체 내역 출력"""
def show_entries(expenses):
    print("\n[전체 내역]")
    if not expenses:
        print("등록된 항목이 없습니다.\n")
        return

    for idx, item in enumerate(expenses, start=1):
        print(f"{idx}. [{item['유형']}] {item['설명']} - {item['금액']}원")
    print()

"""현재 잔액 확인"""
def check_balance(expenses):
    # 수입과 지출을 각각 합산하여 잔액 계산
    income = sum(item['금액'] for item in expenses if item['유형'] == '수입')
    expense = sum(item['금액'] for item in expenses if item['유형'] == '지출')
    balance = income - expense

    print("\n[잔액 확인]")
    print(f"총 수입: {income}원")
    print(f"총 지출: {expense}원")
    print(f"현재 잔액: {balance}원\n")

"""가계부 데이터 저장"""
def save_data(expenses, filename="tracker.txt"):
    with open(filename, mode="w", encoding="utf-8") as file:
        for item in expenses:
            line = f"{item['유형']} | {item['설명']} | {item['금액']}\n"
            file.write(line)

"""가계부 데이터 불러오기"""
def load_data(filename="tracker.txt"):
    if not os.path.exists(filename):
        return []
    loaded = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                entry_type, description, amount = parts
                try:
                    loaded.append({
                        "유형": entry_type,
                        "설명": description,
                        "금액": float(amount)
                    })
                except ValueError:
                    continue  # 금액 변환 실패 시 무시
    return loaded

"""가계부 데이터 초기화"""
def reset_data(expenses, filename="tracker.txt"):
    while True:
        confirm = input("전체 기록을 초기화하시겠습니까? (y/n) : ")
        check_exit(confirm)
        if confirm.lower() == 'y':
            expenses.clear()  # 메모리 상 데이터 초기화
            with open(filename, mode="w", encoding="utf-8") as file:
                pass  # 파일 비우기
            print("가계부 기록이 초기화되었습니다.\n")
            break
        elif confirm.lower() == 'n':
            print("초기화를 취소했습니다.\n")
            break
        else:
            print("y 또는 n으로 입력해주세요.")

"""메인 메뉴"""
def main():
    show_intro()
    expenses = load_data()
    print("이전 기록을 불러왔습니다.\n" if expenses else "새로운 가계부를 시작합니다.\n")

    while True:
        print("1. 항목 추가")
        print("2. 전체 내역 보기")
        print("3. 잔액 확인")
        print("4. 전체 기록 초기화")
        print("5. 종료")

        choice = input("메뉴를 선택하세요 (1-4) : ")
        check_exit(choice)

        if choice == '1':
            add_entry(expenses)
        elif choice == '2':
            show_entries(expenses)
        elif choice == '3':
            check_balance(expenses)
        elif choice == '4':
            reset_data(expenses)
        elif choice == '5':
            save_data(expenses)
            print("가계부를 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 선택하세요.\n")

if __name__ == "__main__":
    main()