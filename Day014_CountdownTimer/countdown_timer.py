import tkinter as tk
from tkinter import messagebox
import threading
import time

# 타이머 제어 변수
stop_flag = False
current_seconds = 0
timer_thread = None
is_running = False

"""countdown_timer"""
def count_timer():
    global stop_flag, current_seconds, is_running
    try:
        # 타이머 처음 실행 시 입력값 처리
        if current_seconds <= 0:
            input_text = entry.get().strip()
            if not input_text.isdigit() or int(input_text) <= 0:
                raise ValueError("올바르지 않은 숫자")

            current_seconds = int(input_text)

        stop_flag = False

        while current_seconds >= 0:
            if stop_flag:
                break
            if not root.winfo_exists():
                break

            mins, secs = divmod(current_seconds, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            timer_label.after(0, timer_label.config, {'text': time_str})
            time.sleep(1)
            current_seconds -= 1

        if current_seconds < 0:
            current_seconds = 0
            timer_label.after(0, timer_label.config, {'text': "00:00"})

        if not stop_flag and root.winfo_exists():
            messagebox.showinfo("⏰ 타이머 종료", "시간이 다 되었습니다!")

        # 종료 후 상태 리셋
        is_running = False
        toggle_button.config(text="▶ 시작")

    except ValueError:
        current_seconds = -1
        is_running = False
        toggle_button.config(text="▶ 시작")
        if root.winfo_exists():
            messagebox.showerror("⚠️입력 오류", "1 이상의 숫자를 입력해주세요.")

"""실행 타이머"""
def start_timer_thread():
    global timer_thread
    if timer_thread and timer_thread.is_alive():
        return
    timer_thread = threading.Thread(target=count_timer, daemon=True)
    timer_thread.start()

"""중지 타이머"""
def stop_timer():
    global stop_flag, timer_thread
    if not stop_flag:
        stop_flag = True
        mins, secs = divmod(current_seconds, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        timer_label.config(text=time_str)
        timer_thread = None

"""시작/중지 토글"""
def toggle_timer():
    global is_running
    if not is_running:
        start_timer_thread()
        is_running = True
        toggle_button.config(text="⏸ 중단")
    else:
        stop_timer()
        is_running = False
        toggle_button.config(text="▶ 시작")

"""초기화 타이머"""
def reset_timer():
    global stop_flag, current_seconds, is_running
    stop_flag = True
    current_seconds = -1
    is_running = False
    timer_label.config(text="00:00")
    entry.delete(0, tk.END)
    toggle_button.config(text="▶ 시작")

"""GUI 설정"""
# 메인 윈도우
root = tk.Tk()
root.title("Countdown Timer ⏳")
root.geometry("300x230")

# 입력 안내 레이블
entry_label = tk.Label(root, text="초 단위 시간 입력")
entry_label.pack(pady=5)

# 시간 입력 필드
entry = tk.Entry(root, justify="center")
entry.pack()

# 버튼 프레임
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# 시작/중단 토글 버튼
toggle_button = tk.Button(button_frame, text="▶ 시작", width=8, command=toggle_timer)
toggle_button.grid(row=0, column=0, columnspan=2, padx=5)

# 초기화 버튼
reset_button = tk.Button(button_frame, text="🔄 초기화", width=8, command=reset_timer)
reset_button.grid(row=0, column=2, padx=5)

# 타이머 표시 레이블
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 28))
timer_label.pack(pady=10)

# GUI 이벤트 루프 실행
root.mainloop()