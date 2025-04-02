import random
import string
import time

"""인트로 출력"""
def intro():
    print("\n🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐")
    print("🔐🔐🔐🔐 비밀번호 생성기 🔐🔐🔐🔐")
    print("🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐\n")

"""무작위 비밀번호 생성 함수"""
def generate_password(length, use_upper, use_digits, use_specials):
    # 기본 소문자
    characters = list(string.ascii_lowercase)
    # 조건에 따라 추가 문자 조합
    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()-_=+[]{}<>?")
    # 안전하게 섞어서 무작위 추출
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

"""간단한 로딩 애니메이션"""
def loading_animation(seconds=1.0):
    print("\n🧪 비밀번호 생성 중", end="", flush=True)
    for _ in range(int(seconds * 4)):  # 0.25초 간격 점 출력
        time.sleep(0.25)
        print(".", end="", flush=True)
    print("\n")

"""password_generator"""
def main():
    intro()
    while True:
        # 사용자 입력
        while True:
            try:
                length = int(input("\n비밀번호 길이를 입력하세요 (4~64) : "))
                if length < 4 or length > 64:
                    print("❌ 비밀번호는 4자 이상 64자 이하로 설정해주세요.\n")
                    continue
                break
            except ValueError:
                print("❌ 숫자를 입력하세요.\n")

        # 대문자 포함 여부
        while True:
            upper_input = input("대문자를 포함할까요? (y/n) : ").lower()
            if upper_input in ('y', 'n'):
                use_upper = upper_input == 'y'
                break
            else:
                print("❌ y 또는 n만 입력해주세요.")

        # 숫자 포함 여부
        while True:
            digit_input = input("숫자를 포함할까요? (y/n) : ").lower()
            if digit_input in ('y', 'n'):
                use_digits = digit_input == 'y'
                break
            else:
                print("❌ y 또는 n만 입력해주세요.")

        # 특수문자 포함 여부
        while True:
            special_input = input("특수문자를 포함할까요? (y/n) : ").lower()
            if special_input in ('y', 'n'):
                use_specials = special_input == 'y'
                break
            else:
                print("❌ y 또는 n만 입력해주세요.")

        # 비밀번호 생성 애니메이션
        loading_animation()

        password = generate_password(length, use_upper, use_digits, use_specials)
        print(f"🔐 생성된 비밀번호 : \033[92m{password}\033[0m")  # 초록색 강조

        # 재생성 여부
        while True:
            again = input("\n🔁 다시 생성할까요? (y/n) : ").lower()
            if again in ('y', 'n'):
                break
            else:
                print("❌ y 또는 n만 입력해주세요.")

        if again == 'n':
            print("\n👋 프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()