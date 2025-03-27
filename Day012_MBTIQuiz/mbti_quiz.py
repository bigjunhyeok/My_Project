import random

"""질문 리스트"""
questions = [
    # E vs I
    ("사람들과 함께 있을 때 에너지가 생긴다", "E", "혼자 있는 시간이 더 편하다", "I"),
    ("말하기 전에 행동하는 편이다", "E", "행동하기 전에 깊이 생각한다", "I"),
    ("파티나 모임을 즐긴다", "E", "조용한 환경에서 휴식하는 걸 선호한다", "I"),
    ("여러 사람들과 어울리는 걸 좋아한다", "E", "소수의 친한 사람과 깊게 지내는 걸 선호한다", "I"),
    ("생각은 말하면서 정리된다", "E", "혼자 생각을 정리한 후 말하는 편이다", "I"),
    # S vs N
    ("현실적이고 구체적인 정보를 신뢰한다", "S", "추상적이고 미래지향적인 아이디어에 끌린다", "N"),
    ("경험을 중시하고 사실에 집중한다", "S", "상상과 가능성에 관심이 많다", "N"),
    ("지금 눈앞에 있는 것에 집중한다", "S", "큰 그림과 전체 흐름을 본다", "N"),
    ("단계적인 설명을 선호한다", "S", "은유나 개념적 설명을 좋아한다", "N"),
    ("실용적인 해결책을 선호한다", "S", "새롭고 창의적인 접근을 시도한다", "N"),
    # T vs F
    ("논리적으로 문제를 분석한다", "T", "감정적으로 공감하며 접근한다", "F"),
    ("결정할 때 객관적인 기준을 우선한다", "T", "사람들의 감정을 고려한다", "F"),
    ("비판적인 피드백을 수용하는 편이다", "T", "피드백을 감정적으로 받아들이는 편이다", "F"),
    ("효율과 성과가 중요하다", "T", "사람 사이의 조화가 중요하다", "F"),
    ("갈등이 생기면 직접적으로 말한다", "T", "상대 기분을 고려하며 조심스럽게 접근한다", "F"),
    # J vs P
    ("일정을 세워 계획대로 움직이는 걸 좋아한다", "J", "상황에 따라 유연하게 움직이는 걸 선호한다", "P"),
    ("해야 할 일을 미리 끝내는 편이다", "J", "마감 직전에 몰아서 하는 편이다", "P"),
    ("정리된 환경에서 일하는 걸 선호한다", "J", "약간 어수선해도 괜찮다", "P"),
    ("선택을 빠르게 결정하고 고수한다", "J", "여러 가능성을 열어두고 유동적으로 결정한다", "P"),
    ("계획을 어기는 걸 싫어한다", "J", "계획은 변할 수 있다고 생각한다", "P")
]

"""인트로 출력"""
def intro():
    print("🎯" * 20)
    print("🎯🎯🎯🎯 간이 MBTI 추천 퀴즈 🎯🎯🎯🎯")
    print("🎯" * 20)

"""메뉴 출력"""
def show_menu():
    print("\n" + "-" * 10)
    print("[메뉴]")
    print("1. MBTI 퀴즈 시작")
    print("2. 종료")
    print("-" * 10)
    return input("\n메뉴 선택 (1/2) : ").strip()

"""질문지 포맷"""
def ask_question(question, option_a, option_b, type_a, type_b):
    print("\n" + "-" * 10)
    print(f"{question}")
    print(f"  A. {option_a} ({type_a})")
    print(f"  B. {option_b} ({type_b})")
    print("-" * 10)
    while True:
        answer = input("선택 (A/B) : ").strip().upper()
        if answer == 'A':
            return type_a
        elif answer == 'B':
            return type_b
        else:
            print("❗ A 또는 B만 입력해주세요.")

"""질문"""
def run_quiz():
    # 점수 초기화
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    # 질문 리스트 섞기 (원본을 해치지 않기 위해 복사 후 섞기)
    randomized_questions = questions.copy()
    random.shuffle(randomized_questions)

    # 모든 질문 순회
    for idx, (option_a, type_a, option_b, type_b) in enumerate(randomized_questions, start=1):
        print(f"\n질문 {idx}")
        print("-" * 30)
        print(f"A. {option_a} ({type_a})")
        print(f"B. {option_b} ({type_b})")
        print("-" * 30)
        while True:
            answer = input("선택 (A/B) : ").strip().upper()
            if answer == 'A':
                scores[type_a] += 1
                break
            elif answer == 'B':
                scores[type_b] += 1
                break
            else:
                print("❗ A 또는 B만 입력해주세요.")

    # 각 축별 결과 계산
    ei = 'E' if scores['E'] >= scores['I'] else 'I'
    sn = 'S' if scores['S'] >= scores['N'] else 'N'
    tf = 'T' if scores['T'] >= scores['F'] else 'F'
    jp = 'J' if scores['J'] >= scores['P'] else 'P'

    # MBTI 조합
    mbti = ei + sn + tf + jp

    # 각 축별 비율 계산
    def get_ratio(a, b):
        total = scores[a] + scores[b]
        if total == 0:
            return (0, 0)
        return (round(scores[a] / total * 100), round(scores[b] / total * 100))

    e_ratio, i_ratio = get_ratio('E', 'I')
    s_ratio, n_ratio = get_ratio('S', 'N')
    t_ratio, f_ratio = get_ratio('T', 'F')
    j_ratio, p_ratio = get_ratio('J', 'P')

    print("\n" + "🧠" * 24)
    print(f"🧠🧠🧠🧠 당신의 MBTI 추천 유형은 💡 {mbti} 입니다! 🧠🧠🧠🧠")
    print("🧠" * 24)

    # 비율 출력
    print("\n" + "📊" * 24)
    print(f"[E/I] 외향(E): {e_ratio}%  /  내향(I): {i_ratio}%")
    print(f"[S/N] 감각(S): {s_ratio}%  /  직관(N): {n_ratio}%")
    print(f"[T/F] 사고(T): {t_ratio}%  /  감정(F): {f_ratio}%")
    print(f"[J/P] 계획(J): {j_ratio}%  /  인식(P): {p_ratio}%")
    print("📊" * 24)

"""MBIT_Quiz"""
def mbti_quiz():
    intro()
    while True:
        choice = show_menu()
        if choice == '1':
            run_quiz()
            break
        elif choice == '2':
            print("퀴즈를 종료합니다.👋")
            break
        else:
            print("❗ 유효한 메뉴 번호를 입력해주세요.")

mbti_quiz()