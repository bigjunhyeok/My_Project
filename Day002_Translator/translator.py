from googletrans import Translator, LANGUAGES

"""문장을 영어로 번역"""
def translate_text(text, dest_lang):
    translator = Translator()
    try:
        trans_result = translator.translate(text, dest_lang)    # 번역 수행
        return trans_result.text    # 번역된 결과 반환
    except Exception as e:
        return f"번역 오류 : {e}"   # 번역 오류 시 메시지 반환

"""번역기"""
def translator():
    print("--------------------")
    print("기본 번역기 (종료: 'q')")
    print("지원 언어 :", LANGUAGES) # 지원 언어 코드 출력
    print("--------------------")

    # 번역할 언어 설정
    default_lang = input("번역할 언어를 입력하세요. (예 : ko, en, zh-cn, ja) : ").strip().lower()
    if not default_lang:
        default_lang = "en" # 미입력 시 기본값
        print("언어를 설정하지 않았습니다. 영어로 번역을 시작합니다.")

    while True:
        # 번역할 문장 입력
        text = input("\n문장을 입력하세요 : ")
        if text.lower() == 'q':
            print("번역기 종료.")
            break

        # 번역 실행
        translated_text = translate_text(text,default_lang)
        print(f"번역 결과 : {translated_text}")

if __name__ == "__main__":
    translator()