import time
import threading
import keyboard

running = False
start_time = 0
elapsed_time = 0

def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 100)
    return f"{minutes:02}:{seconds:02}:{milliseconds:02}"

def stopwatch():
    global running, start_time, elapsed_time
    while True:
        if running:
            elapsed_time = time.time() - start_time
        print(f"\r⏱️ {format_time(elapsed_time)}", end="")
        time.sleep(0.1)

def handle_keys():
    global running, start_time, elapsed_time
    while True:
        if keyboard.is_pressed('s'):
            if not running:
                start_time = time.time() - elapsed_time
                running = True
            else:
                running = False
            time.sleep(0.3)

        elif keyboard.is_pressed('r'):
            running = False
            elapsed_time = 0
            print("\r🔁 Reset!", end="")
            time.sleep(0.3)

        elif keyboard.is_pressed('q'):
            print("\n👋 종료합니다.")
            break

# 스레드 실행
threading.Thread(target=stopwatch, daemon=True).start()
handle_keys()
