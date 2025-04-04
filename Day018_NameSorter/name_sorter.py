"""인트로 출력"""
def intro():
    print("=" * 40)
    print("        📛 이름 정렬기 - NameSorter")
    print("=" * 40)

"""이름 입력받기"""
def get_names():
    while True:
        raw_input = input("\n이름들을 쉼표(,)로 구분해서 입력해주세요 : ")
        names = [name.strip() for name in raw_input.split(",") if name.strip()]
        if names:
            return names
        else:
            print("❗ 최소 하나 이상의 이름을 입력해 주세요.\n")

"""정렬 방식 선택"""
def choose_sort_method():
    print("\n정렬 방법을 선택하세요 :")
    print("1. 알파벳 순 정렬.")
    print("2. 이름 길이 순 정렬.")
    while True:
        choice = input("선택 (1 또는 2) : ")
        if choice in ["1", "2"]:
            return choice
        else:
            print("❗ 1 또는 2를 입력하세요.\n")

"""정렬 방향 선택"""
def choose_sort_order():
    print("\n정렬 방향을 선택하세요 :")
    print("1. 오름차순 (A-Z / 짧은 → 긴)")
    print("2. 내림차순 (Z-A / 긴 → 짧은)")
    while True:
        order = input("선택 (1 또는 2): ")
        if order in ["1", "2"]:
            return order
        else:
            print("❗ 1 또는 2를 입력하세요.\n")

"""이름 정렬"""
def sort_names(names, method, order):
    reverse_flag = order == "2"  # 내림차순이면 True
    if method == "1":
        return sorted(names, key=str.lower, reverse=reverse_flag)
    elif method == "2":
        return sorted(names, key=len, reverse=reverse_flag)

"""결과 출력"""
def show_result(sorted_names):
    print("\n" + "=" * 40)
    print("📋 정렬된 이름 목록".center(40))
    print("=" * 40)
    for idx, name in enumerate(sorted_names, start=1):
        print(f"{idx:>2}. ✅ {name}")
    print("=" * 40)
    print("이름 정렬 완료.\n")

"""name_sorter"""
def main():
    intro()
    names = get_names()
    method = choose_sort_method()
    order = choose_sort_order()
    sorted_names = sort_names(names, method, order)
    show_result(sorted_names)

if __name__ == "__main__":
    main()