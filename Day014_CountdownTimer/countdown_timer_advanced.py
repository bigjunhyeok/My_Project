import tkinter as tk
from tkinter import messagebox
import threading
import time

# 타이머 제어 변수
stop_flag = False
current_seconds = 0
timer_thread = None
is_running = False
pause_logs = []  # ⏸ 중단 시간 기록용 리스트

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
            if stop_flag or not root.winfo_exists():
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

        # 상태 리셋
        is_running = False
        toggle_button.config(text="▶ 시작")

    except ValueError:
        current_seconds = -1
        is_running = False
        toggle_button.config(text="▶ 시작")
        if root.winfo_exists():
            messagebox.showerror("⚠️입력 오류", "1 이상의 숫자를 입력해주세요.")

"""타이머 실행"""
def start_timer_thread():
    global timer_thread
    if timer_thread and timer_thread.is_alive():
        return
    timer_thread = threading.Thread(target=count_timer, daemon=True)
    timer_thread.start()

"""타이머 중지"""
def stop_timer():
    global stop_flag, timer_thread
    if not stop_flag:
        stop_flag = True
        mins, secs = divmod(current_seconds, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        timer_label.config(text=time_str)
        timer_thread = None

        # ✅ 중단 시간 기록
        pause_logs.append(time_str)
        log_listbox.insert(tk.END, f"⏸ 중단 시각: {time_str}")

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

"""타이머 초기화"""
def reset_timer():
    global stop_flag, current_seconds, is_running
    stop_flag = True
    current_seconds = -1
    is_running = False
    timer_label.config(text="00:00")
    entry.delete(0, tk.END)
    toggle_button.config(text="▶ 시작")
    log_listbox.delete(0, tk.END)
    pause_logs.clear()

"""기록 선택 시 해당 시간으로 설정"""
def on_log_select(event):
    global current_seconds, is_running
    if not log_listbox.curselection():
        return
    selected = log_listbox.get(log_listbox.curselection())
    if "⏸ 중단 시각:" in selected:
        time_str = selected.replace("⏸ 중단 시각: ", "")
        try:
            mins, secs = map(int, time_str.split(":"))
            current_seconds = mins * 60 + secs
            entry.delete(0, tk.END)
            entry.insert(0, str(current_seconds))
            timer_label.config(text=f"{mins:02d}:{secs:02d}")
            toggle_button.config(text="▶ 시작")
            is_running = False
        except:
            pass

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
timer_label.pack(pady=5)

# 중단 기록
log_label = tk.Label(root, text="⏸ 중단 기록")
log_label.pack()

log_listbox = tk.Listbox(root, height=4)
log_listbox.pack(pady=5)
log_listbox.bind("<<ListboxSelect>>", on_log_select)

# GUI 이벤트 루프 실행
root.mainloop()