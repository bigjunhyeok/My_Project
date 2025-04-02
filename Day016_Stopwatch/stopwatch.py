import time
import threading
import keyboard

# 전역 변수
running = False
start_time = 0
elapsed_time = 0
lap_times = []  # 일시정지 시점 기록 리스트

"""시간을 MM:SS:ms 형식으로 포맷팅"""
def format_time(total_seconds):
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 100)
    return f"{minutes:02}:{seconds:02}:{milliseconds:02}"

"""스톱워치 실행 쓰레드"""
def stopwatch():
    global running, start_time, elapsed_time
    while True:
        if running:
            elapsed_time = time.time() - start_time
        print(f"\r⏱️  {format_time(elapsed_time)}", end="", flush=True)
        time.sleep(0.1)

"""인트로 출력 함수"""
def intro():
    print("\n🕒🕒🕒🕒🕒🕒🕒🕒🕒🕒🕒🕒🕒")
    print("🕒🕒🕒🕒 Stopwatch 🕒🕒🕒🕒")
    print("🕒🕒🕒🕒🕒🕒🕒🕒🕒🕒🕒🕒🕒\n")

    print(" ▶ S 키 : 시작/일시정지")
    print(" ▶ R 키 : 리셋")
    print(" ▶ Q 키 : 종료\n")

"""사용자 키 입력을 처리하는 함수"""
def handle_keys():
    global running, start_time, elapsed_time, lap_times

    while True:
        if keyboard.is_pressed('s'):
            if not running:
                start_time = time.time() - elapsed_time
                running = True
            else:
                running = False
                # 📝 일시정지할 때마다 랩타임 기록
                lap_times.append(format_time(elapsed_time))
            time.sleep(0.3)  # 연속 입력 방지

        elif keyboard.is_pressed('r'):
            running = False
            elapsed_time = 0
            if lap_times:
                print("\n" + "-" * 30)
                print("📋 전체 기록 :")
                for i, t in enumerate(lap_times, 1):
                    print(f"  {i:>2}) {t}")
                print("-" * 30)
            lap_times = []
            print("\r🔁 초기화 완료.          ", end="", flush=True)
            time.sleep(0.3)

        elif keyboard.is_pressed('q'):
            print("\n\n👋 프로그램을 종료합니다.")
            if lap_times:
                print("\n" + "-" * 30)
                print("📋 전체 기록 :")
                for i, t in enumerate(lap_times, 1):
                    print(f"  {i:>2}) {t}")
                print("-" * 30)
            break

"""stopwatch"""
def main():
    intro()

    threading.Thread(target=stopwatch, daemon=True).start()
    handle_keys()

if __name__ == "__main__":
    main()