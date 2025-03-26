import random
import time

"""컵 섞기"""
def shuffle_cups():
    cups = ["-", "-", "💰"]  # 랜덤
    random.shuffle(cups)
    return cups

"""야바위 게임"""
def play_shell_game():
    win_count = 0  # 승리 횟수 저장
    lose_count = 0  # 패배 횟수 저장

    print("🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩")
    print("🎩🎩🎩🎩 야바위 게임 🎩🎩🎩🎩")
    print("🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩")
    time.sleep(1)

    # 게임 설명
    shell_game_intro = [
        "\n############################################################",
        "플레이어는 여러 개의 컵 중 공을 숨긴 컵의 위치를 맞혀야 합니다.",
        "",
        "✅ 게임 규칙 :",
        "1. 컵은 3개이며, 각각 왼쪽부터 번호(1번부터 3번)가 매겨져 있습니다.",
        "2. 공은 무작위로 하나의 컵에 숨겨집니다.",
        "3. 플레이어는 컵의 번호를 입력하여 공의 위치를 추측합니다.",
        "",
        "자 이제 게임을 시작합니다!",
        "############################################################"
    ]
    for line in shell_game_intro:
        print(line)
        time.sleep(0.3)

    while True:
        print("\n------------------------")
        cups = shuffle_cups()  # 컵 섞기
        print("🎲 컵을 섞는 중입니다...\n")
        time.sleep(2)

        print("🥤 🥤 🥤")  # 컵 3개 출력

        # 게임 수행
        while True:
            try:
                choice = int(input("\n🔍 동전이 들어있는 컵을 선택하세요 (1, 2, 3) : "))
                if 1 <= choice <= 3:
                    break
                else:
                    print("\n⚠️유효하지 않은 값입니다. 다시 입력하세요.")
            except ValueError:
                print("\n⚠️유효하지 않은 값입니다. 다시 입력하세요.")

        index = choice - 1  # cups 리스트 인덱스 맞추기
        selected_cup = cups[index]  # 플레이어가 선택한 컵

        if selected_cup == "💰":
            print(f"\n🔥 정답! 당신의 승리입니다.\n 정답 : {cups}")
            win_count += 1 # 승리 횟수 카운트
        else:
            print(f"\n💥 꽝! 당신의 패배입니다.\n 정답 : {cups}")
            lose_count += 1 # 패배 횟수 카운트

        # 게임 재시도 선택
        while True:
            retry = input("\n다시 하시겠습니까? (y/n) : ").strip().lower()
            if retry in ["y"]:
                break
            elif retry in ["n"]:
                print("\n👋 게임을 종료합니다.")
                print("\n---------------")
                print(f"🔢 총 게임 수: {win_count + lose_count}")
                print("---------------")
                print(f"🏆 승리 횟수 : {win_count}")
                print(f"💀 패배 횟수 : {lose_count}")
                win_rate = int((win_count / (win_count + lose_count)) * 100)
                print("---------------")
                print(f"📊 승률 : {win_rate}%")
                print("---------------")
                return
            else:
                print("\n잘못된 입력입니다.")

if __name__ == "__main__":
    play_shell_game()