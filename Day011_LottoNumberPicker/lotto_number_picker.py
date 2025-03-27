import random

"""1~45 사이 숫자 중 중복 없이 6개 랜덤 추첨"""
def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

"""인트로 출력"""
def show_intro():
    print("\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯")
    print("🎯🎯🎯🎯 로또 번호 생성기 🎯🎯🎯🎯")
    print("🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯")

"""lotto_number_picker"""
def main():
    show_intro()

    while True:
        user_input = input("\n엔터를 누르면 로또 번호가 생성됩니다 : (종료 q)")
        if user_input.lower() == 'q':
            print("\n👋 프로그램을 종료합니다.")
            break

        # 번호 리스트
        history = []

        # 번호 생성
        while True:
            numbers = generate_lotto_numbers()
            history.append(numbers)

            print("-" * 40)
            print(f"👉 생성된 번호 [{len(history)}회차] :", numbers)
            print("-" * 40)

            # 재추첨 여부 묻기
            while True:
                retry_input = input("\n다시 뽑으시겠습니까? (재추첨 r / 기록보기 h / 종료 q) : ").lower()

                if retry_input == 'r':
                    break  # 재추첨
                elif retry_input == 'h':
                    if history:
                        print("\n📜 전체 생성 기록 :")
                        for idx, record in enumerate(history, start=1):
                            print(f"  {idx}회차 :", record)
                        print("-" * 40)
                    else:
                        print("\n📭 아직 생성된 번호가 없습니다.")
                elif retry_input == 'q':
                    print("\n👋 프로그램을 종료합니다.")
                    return  # 종료
                else:
                    print("\n❗ 잘못된 입력입니다. 'r', 'n', 'q' 중 하나를 입력해주세요.")

if __name__ == "__main__":
    main()