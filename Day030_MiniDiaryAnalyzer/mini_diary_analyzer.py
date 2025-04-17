import os
import re

# 감정 단어 사전 (원형 기준, 어근 형태)
POSITIVE_WORDS = {
    '행복', '기쁨', '좋', '즐겁', '감사', '사랑', '재밌', '신나', '기대',
    '뿌듯', '감동', '웃', '설렘', '만족', '편안', '평온', '흥미', '자랑',
    '성취', '긍정', '사려깊', '칭찬', '안도', '감격', '유쾌', '환희'
}
NEGATIVE_WORDS = {
    '슬픔', '짜증', '화나', '싫', '불안', '우울', '불편', '지치', '외롭',
    '힘들', '괴롭', '속상', '불쾌', '비참', '절망', '분노', '실망', '초조',
    '억울', '한숨', '눈물', '시무룩', '고통', '좌절', '짜증', '낙담', '부정'
}

# 조사/어미 제거용 패턴 (간단 버전)
ENDING_PATTERN = re.compile(r'(았|었|다|해|고|서|네|지|요|자|며|는|을|를|가|이|은|에|의|도|으로|하고|해서)?$')

'''인트로 출력'''
def show_intro():
    print('=' * 42)
    print('      일기 분석기 (Mini Diary Analyzer)')
    print(' - 단어 수, 감정 단어 비율, 긍/부정 분석 제공 -')
    print('=' * 42)

'''단어에서 어미/조사 제거 (원형 추출 흉내)'''
def normalize_word(word):
    return ENDING_PATTERN.sub('', word)

'''분석 로직'''
def analyze_diary(text):
    raw_words = re.findall(r'\b[\w가-힣]+\b', text)
    total_word_count = len(raw_words)

    normalized_words = [normalize_word(word) for word in raw_words]

    # 감정 단어 탐지: startswith 방식으로 유연하게 처리
    emotion_words = [word for word in normalized_words
                     if any(word.startswith(pos) for pos in POSITIVE_WORDS)
                     or any(word.startswith(neg) for neg in NEGATIVE_WORDS)]

    positive_count = sum(1 for word in normalized_words
                         if any(word.startswith(pos) for pos in POSITIVE_WORDS))
    negative_count = sum(1 for word in normalized_words
                         if any(word.startswith(neg) for neg in NEGATIVE_WORDS))

    return {
        'total_words': total_word_count,
        'emotion_words': len(emotion_words),
        'positive': positive_count,
        'negative': negative_count
    }

'''분석 결과 출력'''
def print_analysis(result):
    print('\n[분석 결과]')
    print(f"- 총 단어 수         : {result['total_words']}")
    print(f"- 감정 단어 수       : {result['emotion_words']}")
    print(f"- 긍정 단어 수       : {result['positive']}")
    print(f"- 부정 단어 수       : {result['negative']}")

    if result['positive'] > result['negative']:
        print("- 감정 판단          : 긍정적인 일기")
    elif result['positive'] < result['negative']:
        print("- 감정 판단          : 부정적인 일기")
    else:
        print("- 감정 판단          : 중립적인 일기")

'''MiniDiaryAnalyzer'''
def main():
    show_intro()

    filename = input('\n분석할 일기 텍스트 파일명을 입력하세요 (.txt) : ').strip()
    if not filename.endswith('.txt'):
        filename += '.txt'

    if not os.path.isfile(filename):
        print(f"오류 : 파일 '{filename}' 을(를) 찾을 수 없음")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        diary_text = f.read()

    result = analyze_diary(diary_text)
    print_analysis(result)

if __name__ == '__main__':
    main()