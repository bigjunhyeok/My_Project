import random

"""칭찬 리스트"""
compliments = [
    "오늘도 멋져요!",
    "당신은 대단한 사람입니다!",
    "좋은 에너지가 느껴져요!",
    "항상 노력하는 모습이 인상적이에요.",
    "당신의 미소는 모두를 행복하게 해요.",
    "당신의 아이디어는 참신하고 멋져요!",
    "어떤 일이든 잘 해낼 수 있어요.",
    "항상 응원하고 있어요!"
]

"""무작위 칭찬 반환"""
def get_compliment(name=None):
    compliment = random.choice(compliments)
    if name:
        return f"{name}님, {compliment}"
    else:
        return compliment

"""리스트에 칭찬 추가"""
def add_compliment():
    new_compliment = input("추가할 칭찬 문구를 입력하세요 : ").strip()
    if new_compliment:
        compliments.append(new_compliment)
        print("✅ 칭찬이 추가되었습니다.")
    else:
        print("⚠️빈 값은 추가할 수 없습니다.")

"""리스트에서 칭찬 삭제"""
def del_compliment():
    print("\n[현재 칭찬 목록]")
    for i, c in enumerate(compliments, 1):
        print(f"{i}. {c}")
    try:
        index = int(input("삭제할 칭찬 번호를 입력하세요 : "))
        if 1 <= index <= len(compliments):
            removed = compliments.pop(index - 1)
            print(f"🗑️ 삭제된 칭찬 : {removed}")
        else:
            print("⚠️올바른 번호를 입력하세요.")
    except ValueError:
        print("⚠️숫자를 입력해주세요.")

"""메뉴 출력"""
def show_menu():
    print("\n📋 메뉴")
    print("1. 랜덤 칭찬")
    print("2. 칭찬 추가")
    print("3. 칭찬 삭제")
    print("4. 종료")

"""compliment_generator"""
if __name__ == "__main__":
    name_input = input("이름을 입력해주세요 : ").strip()
    print("\n" + get_compliment(name_input if name_input else None))