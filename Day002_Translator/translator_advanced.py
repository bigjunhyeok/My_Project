from googletrans import Translator, LANGUAGES

"""문장을 영어로 번역"""
def translate_text(text, dest_lang="ko", show_option=False):
    translator = Translator()
    try:
        trans_result = translator.translate(text, src="auto", dest=dest_lang)   # 언어 자동 감지 및 번역 수행
        detected_lang = trans_result.src    # 감지된 언어
        translated_text = trans_result.text # 번역된 문장

        # 옵션 출력 여부 설정
        if show_option:
            return f"[{detected_lang}] {text} ➝ {translated_text}"  # 감지된 언어 + 원본 + 번역된 문장
        else:
            return translated_text  # 번역된 문장

    except Exception as e:
        return f"번역 오류 : {e}"    # 오류 발생 시 기본값 반환

"""한글 번역기"""
def translator():
    print("--------------------")
    print("한글 번역기 (종료: 'q', 기록 : 'history', 초기화 : 'clear', 옵션변경 : 'option', 상세정보 : 'detail' )")
    print("입력된 문장을 자동으로 감지하여 한글로 번역하는 서비스입니다.")
    print("번역 기록이 모두 저장되며, 초기화가 가능합니다.")
    print("--------------------")

    history = []  # 번역 기록 저장 리스트
    show_option = False # 옵션 출력 여부

    while True:
        # 번역할 문장 입력
        text = input("\n문장을 입력하세요 : ").strip()

        if text == "":
            continue

        if text.lower() == 'q': # 종료
            print("번역기 종료.")
            break

        if text.lower() == 'history':   # 기록 확인
            if not history:
                print("기록이 없습니다.")
            else:
                print("\n 번역 기록 ")
                print("============")
                for idx, translated in enumerate(history, 1):
                    print(f"{idx}. {translated}")
                print("============")
            continue

        if text.lower() == 'clear': # 기록 초기화
            history.clear()
            print("번역 기록이 초기화되었습니다.")
            continue

        if text.lower() == 'option':    # 옵션 출력 여부 상태 변경
            show_option = not show_option
            print(f"옵션 출력 여부 : {'ON' if show_option else 'OFF'}")
            continue

        if text.lower() == 'detail':   # 상세 정보 출력
            print("\n 상세 정보")
            print("###########")
            print(f"기록된 문장 수 : {len(history)}개")
            print(f"옵션 출력 여부 : {'ON' if show_option else 'OFF'}")
            print("###########")
            continue

        # 번역 실행
        translated_result = translate_text(text, "ko", show_option)
        print(translated_result)
        history.append(translated_result)

if __name__ == "__main__":
    translator()