"""단위별 변환 비율 저장"""
conversion_rates = {
    ('cm', 'inch'): 1 / 2.54,
    ('inch', 'cm'): 2.54,
    ('kg', 'lb'): 2.20462,
    ('lb', 'kg'): 1 / 2.20462,
    ('km', 'mile'): 0.621371,
    ('mile', 'km'): 1 / 0.621371,
}

"""단위 변환 함수"""
def convert(value, from_unit, to_unit):
    key = (from_unit, to_unit)
    if key in conversion_rates:
        return value * conversion_rates[key]
    else:
        raise ValueError("지원하지 않는 단위 변환입니다.")

"""전체 단위 변환 함수"""
def convert_all(value):
    print("\n📊 전체 단위 변환 결과:")
    for (from_unit, to_unit), rate in conversion_rates.items():
        result = convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result:.2f} {to_unit}")
    print()

"""메뉴 출력"""
def show_menu():
    print("\n📐📐📐📐📐📐📐📐📐📐📐📐📐📐📐")
    print("📐📐📐📐 단위 변환기 📐📐📐📐")
    print("📐📐📐📐📐📐📐📐📐📐📐📐📐📐📐\n")
    print("-------------------------")
    for i, (from_unit, to_unit) in enumerate(conversion_rates.keys(), 1):
        print(f"{i}. {from_unit} → {to_unit}")
    print("7. 전체 변환")
    print("0. 종료")
    print("-------------------------")

"""UnitConverter"""
def main():
    keys = list(conversion_rates.keys())

    while True:
        # 메뉴 출력
        show_menu()
        choice = input("번호를 선택하세요 : ").strip()
        # 프로그램 종료
        if choice == '0':
            print("👋 프로그램을 종료합니다.")
            break

        # 값 입력
        try:
            value = float(input("\n변환할 값을 입력하세요 : "))
        except ValueError:
            print("❗ 유효한 번호를 입력해주세요.")
            continue

        # 전체 단위 변환
        if choice == '7':
            convert_all(value)

        # 단위 변환
        elif choice.isdigit() and (1 <= int(choice) <= len(keys)):
            from_unit, to_unit = keys[int(choice) - 1]
            result = convert(value, from_unit, to_unit)
            # 결과 출력
            print(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            print("❗ 유효한 번호를 입력해주세요.")
            continue

        # 재시작 여부
        while True:
            again = input("\n다시 변환하시겠습니까? (y/n) : ").strip().lower()
            if again == 'y':
                break
            elif again == 'n':
                print("👋 프로그램을 종료합니다.")
                return
                sys.exit()
            else:
                print("❗ 유효한 값을 입력해주세요.")

if __name__ == "__main__":
    main()