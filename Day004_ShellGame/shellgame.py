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

    while True:
        cups = shuffle_cups()  # 컵 섞기
        print("\n🎲 컵을 섞는 중...\n")
        time.sleep(2)

        print("🥤 🥤 🥤")  # 컵 3개 출력

        while True:
            try:
                choice = int(input("🔍 동전이 들어있는 컵 선택 (1, 2, 3) : "))
                if 1 <= choice <= 3:
                    break
                else:
                    print("\n 유효하지 않은 값. 다시 입력.")
            except ValueError:
                print("\n 유효하지 않은 값. 다시 입력.")

        index = choice - 1  # cups 리스트 인덱스 맞추기
        selected_cup = cups[index]  # 플레이어가 선택한 컵

        if selected_cup == "💰":
            print(f"\n🔥 정답! 당신의 승리.\n 정답 : {cups}")
            win_count += 1 # 승리 횟수 카운트
        else:
            print(f"\n💥 꽝! 당신의 패배.\n 정답 : {cups}")
            lose_count += 1 # 패배 횟수 카운트

        # 게임 재시도 선택
        while True:
            retry = input("\n다시 하시겠습니까? (y/n) : ").strip().lower()
            if retry in ["y"]:
                break
            elif retry in ["n"]:
                print("\n----------")
                print(f"🔢 총 게임 수: {win_count + lose_count}")
                print("----------")
                print(f"🏆 승리 횟수 : {win_count}")
                print(f"💀 패배 횟수 : {lose_count}")
                win_rate = int((win_count / (win_count + lose_count)) * 100)
                print("----------")
                print(f"📊 당신의 승률 : {win_rate}%")
                print("----------")
                print("\n👋 게임을 종료합니다. 감사합니다!")
                return
            else:
                print("\n잘못된 입력.")

if __name__ == "__main__":
    play_shell_game()