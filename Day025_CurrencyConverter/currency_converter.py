"""고정 환율 정보 (KRW 기준)"""
rates_to_krw = {
    "KRW": 1,
    "USD": 1333.33,
    "EUR": 1470.59,
    "JPY": 9.09
}

"""인트로 출력"""
def show_intro():
    print("💱" * 16)
    print("💱💱💱💱 오늘의 환율 계산기 💱💱💱💱")
    print("💱" * 16)

"""메인 출력"""
def show_main():
    print("\n📊 ---- 오늘의 환율 ----")
    print(f"{'CURRENCY':<10} {'→ KRW':>10}")
    print("-" * 24)
    for currency, rate in rates_to_krw.items():
        print(f"{currency:<10} {rate:>10.2f}")
    print("-" * 24)

"""환율을 반영한 금액"""
def convert_currency(amount, from_currency, to_currency):
    try:
        # Step 1: from → KRW
        amount_in_krw = amount * rates_to_krw[from_currency]
        # Step 2: KRW → to
        converted = amount_in_krw / rates_to_krw[to_currency]
        return converted, amount_in_krw
    except KeyError:
        return None, None

"""지원 통화 코드 확인"""
def is_supported_currency(code):
    return code in rates_to_krw

"""CurrencyConverter"""
def main():
    while True:
        # 변환할 통화 코드 입력
        while True:
            from_currency = input("\n변환할 통화 (KRW, USD, EUR, JPY) : ").upper()
            if is_supported_currency(from_currency):
                break
            else:
                print("❗ 지원하지 않는 통화입니다. 다시 입력하세요.")

        # 변환될 통화 코드 입력
        while True:
            to_currency = input("변환될 통화 (KRW, USD, EUR, JPY) : ").upper()
            if is_supported_currency(to_currency):
                break
            else:
                print("❗ 지원하지 않는 통화입니다. 다시 입력하세요.")

        # 금액 입력
        while True:
            amount_input = input(f"{from_currency} 금액 입력 : ")
            try:
                amount = float(amount_input)
                break
            except ValueError:
                print("⚠️ 숫자만 입력하세요.")

        # 환율 변환
        result, krw_equivalent = convert_currency(amount, from_currency, to_currency)

        if result is None:
            print("\n🚫 변환 정보를 찾을 수 없습니다.")
        else:
            print(f"\n✅ 변환 결과 : {amount} {from_currency} → {result:.2f} {to_currency}")
            print(f"💵 한화 환산 : {krw_equivalent:.2f} KRW")

        # 계속할지 여부 확인
        while True:
            again = input("\n다시 계산하시겠습니까? (Y/N) : ").strip().lower()
            if again == 'y' or again == '':
                break
            elif again == 'n':
                print("👋 환율 계산기를 종료합니다. 감사합니다!")
                return
            else:
                print("❗ Y 또는 N으로만 입력해주세요.")

if __name__ == "__main__":
    show_intro()
    show_main()
    main()