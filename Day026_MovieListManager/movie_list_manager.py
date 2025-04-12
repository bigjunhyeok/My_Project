import os
import json

DATA_FILE = "movies.json"

"""인트로 출력"""
def show_intro():
    print("🎬" * 18)
    print("🎬🎬🎬🎬  보고 싶은 영화 목록  🎬🎬🎬🎬")
    print("🎬" * 18)

"""메뉴 출력"""
def show_menu():
    print("\n---- 영화 목록 관리기 ----")
    print("1. 영화 추가")
    print("2. 목록 보기")
    print("3. 영화 삭제")
    print("4. 전체 삭제")
    print("5. 영화 찾기")
    print("6. 종료")
    print("------------------------")

"""영화 검색"""
def search_movies(movie_list):
    if not movie_list:
        print("📂 현재 등록된 영화가 없습니다.")
        return

    print("\n🔍 검색 기준을 선택하세요")
    print("1. 제목")
    print("2. 감독")
    print("3. 출연진")
    print("4. 개봉연도")

    # 검색 기준 선택 반복
    while True:
        choice = input("선택 (1~4): ").strip()
        if choice in ['1', '2', '3', '4']:
            break
        print("❗ 1부터 4 사이의 숫자로 선택해주세요.")

    # 검색어 입력 반복
    while True:
        query = input("검색어 입력 : ").strip().lower()
        if query:
            break
        print("❗ 검색어는 비워둘 수 없습니다.")

    # 결과 찾기
    matched = []

    for movie in movie_list:
        if choice == '1' and query in movie['title'].lower():
            matched.append(movie)
        elif choice == '2' and query in movie['director'].lower():
            matched.append(movie)
        elif choice == '3':
            if any(query in actor.lower() for actor in movie['actors']):
                matched.append(movie)
        elif choice == '4':
            if not query.isdigit():
                print("❗ 개봉연도 검색은 숫자만 입력 가능합니다.")
                return
            if int(query) == movie['year']:
                matched.append(movie)

    if not matched:
        print("🔎 검색 결과가 없습니다.")
    else:
        print(f"\n🎯 검색 결과 ({len(matched)}건):")
        for idx, movie in enumerate(matched, start=1):
            print(f"\n{idx}. 🎬 {movie['title']} ({movie['year']})")
            print(f"   🎬 감독 : {movie['director']}")
            print(f"   🎭 출연 : {', '.join(movie['actors'])}")

"""영화 추가"""
def add_movie(movie_list):
    # 제목 입력
    while True:
        title = input("🎬 영화 제목 : ").strip()
        if not title:
            print("❗ 영화 제목은 필수입니다. 다시 입력해주세요.")
            continue

        # 제목 중복 확인 (대소문자 무시)
        if any(movie['title'].lower() == title.lower() for movie in movie_list):
            print(f"❗ '{title}' 은(는) 이미 목록에 등록되어 있습니다.")
            continue

        break

    # 감독 입력
    while True:
        director = input("🎬 감독 : ").strip()
        if director:
            break
        print("❗ 감독 이름은 필수입니다. 다시 입력해주세요.")

    # 출연진 입력
    actors_input = input("🎭 출연진 (쉼표로 구분, 생략 가능) : ").strip()
    actors = [actor.strip() for actor in actors_input.split(',') if actor.strip()]

    # 연도 입력
    while True:
        year_input = input("📅 개봉 연도 : ").strip()
        if not year_input:
            print("❗ 연도는 필수입니다. 반드시 입력해주세요.")
        elif not year_input.isdigit():
            print("❗ 연도는 숫자(예: 2022)로만 입력 가능합니다.")
        else:
            year = int(year_input)
            break

    # 영화 추가
    movie = {
        "title": title,
        "director": director,
        "actors": actors,
        "year": year
    }
    movie_list.append(movie)
    print(f"✅ '{title}' 이(가) 목록에 추가되었습니다.")

"""영화 목록 보기"""
def show_movies(movie_list):
    if not movie_list:
        print("📂 현재 등록된 영화가 없습니다.")
        return

    print("\n🎞️ 보고 싶은 영화 목록:")
    for idx, movie in enumerate(movie_list, start=1):
        print(f"\n{idx}. 🎬 {movie['title']} ({movie['year']})")
        print(f"   🎬 감독 : {movie['director']}")
        print(f"   🎭 출연 : {', '.join(movie['actors'])}")

"""영화 삭제"""
def delete_movie(movie_list):
    if not movie_list:
        print("📂 현재 등록된 영화가 없습니다.")
        return

    show_movies(movie_list)

    while True:
        user_input = input("\n삭제할 번호 입력 (취소하려면 엔터) : ").strip()

        if not user_input:  # 빈 입력 → 삭제 취소
            print("❎ 삭제를 취소했습니다.")
            return

        if not user_input.isdigit():
            print("❗ 숫자만 입력하세요.")
            continue

        index = int(user_input)
        if 1 <= index <= len(movie_list):
            removed = movie_list.pop(index - 1)
            print(f"🗑️ '{removed['title']}' 삭제 완료.")
            return
        else:
            print(f"❗ 1부터 {len(movie_list)} 사이의 번호를 입력해주세요.")

"""전체 삭제"""
def clear_movies(movie_list):
    movie_list.clear()
    print("🧹 영화 목록이 모두 삭제되었습니다.")

"""영화 목록 저장"""
def save_movies(movie_list):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(movie_list, f, ensure_ascii=False, indent=2)
        #print("💾 영화 목록이 저장되었습니다.")
    except Exception as e:
        print(f"❗ 저장 중 오류 발생: {e}")

"""영화 목록 불러오기"""
def load_movies():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❗ 파일 로딩 실패 : {e}")
    return []

"""MovieListManager"""
def main():
    movie_list = load_movies()

    show_intro()

    while True:
        show_menu()
        choice = input("선택 (1~6) : ").strip()

        if choice == '1':
            add_movie(movie_list)
        elif choice == '2':
            show_movies(movie_list)
        elif choice == '3':
            delete_movie(movie_list)
        elif choice == '4':
            clear_movies(movie_list)
        elif choice == '5':
            search_movies(movie_list)
        elif choice == '6':
            save_movies(movie_list)
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❗ 1~6 중에서 선택해주세요.")

if __name__ == "__main__":
    main()