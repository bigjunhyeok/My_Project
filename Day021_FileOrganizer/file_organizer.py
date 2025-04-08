import os
import shutil

# 정리할 대상 폴더 (현재 폴더 기준)
target_folder = "."

"""파일 이름에 따라 분류할 카테고리 키워드"""
category_map = {
    "업무":    ["report", "plan", "task"],
    "관리":    ["log", "config", "setting"],
    "지식":    ["guide", "manual", "study"],
    "보관":    ["backup", "old", "archive"]
}

"""인트로 출력"""
def show_intro():
    print("📂" * 15)
    print("📂📂📂📂 파일 정리기 📂📂📂📂")
    print("📂" * 15)

"""메뉴 출력"""
def show_menu():
    print("\n[1] 파일 직접 만들기")
    print("[2] 파일 정리 시작")
    print("[0] 종료")

"""파일 직접 입력받아 생성"""
def create_file_by_input():
    filename = input("생성할 파일 이름을 입력하세요 (예: report_2025.txt) : ").strip()
    if not filename:
        print("! 파일 이름이 비어 있습니다.")
        return

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("")  # 빈 파일
    print(f"✅ '{filename}' 파일이 생성되었습니다.")
    print(f"📁 생성된 경로: {os.path.abspath(filename)}")

"""확장자 기준으로 파일 정리"""
def organize_files_by_category():
    files = os.listdir(target_folder)
    current_file = os.path.basename(__file__)
    moved = 0

    for file in files:
        if os.path.isfile(file):
            if file == current_file:
                continue  # 자기 자신은 제외

            file_lower = file.lower()
            destination = "기타"  # 기본값은 '기타'

            # 카테고리 키워드 매칭 시 덮어씀
            for category, keywords in category_map.items():
                if any(keyword in file_lower for keyword in keywords):
                    destination = category
                    break

            # 폴더 생성 후 이동
            folder_path = os.path.join(target_folder, destination)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file, os.path.join(folder_path, file))
            moved += 1

    print(f"✅ 정리 완료! {moved}개의 파일을 카테고리별로 분류했습니다.")

if __name__ == "__main__":
    show_intro()
    while True:
        show_menu()
        choice = input("선택 >> ").strip()
        if choice == "1":
            create_file_by_input()
        elif choice == "2":
            organize_files_by_category()
        elif choice == "0":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("! 잘못된 입력입니다. 다시 선택해주세요.")