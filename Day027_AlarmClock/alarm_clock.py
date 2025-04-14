import time
from datetime import datetime
import platform
import threading
import os

alarms = []
history = []

"""인트로 출력"""
def show_intro():
    print("🔔" * 14)
    print("🔔🔔🔔🔔 알람 시계 🔔🔔🔔🔔")
    print("🔔" * 14)

"""메뉴 출력"""
def show_menu():
    print("\n------------------------")
    print("1. 알람 보기")
    print("2. 알람 설정")
    print("3. 알람 삭제")
    print("4. 히스토리")
    print("5. 종료")
    print("------------------------")

"""알람 울리기"""
def ring_alarm(alarm):
    print(f"\n[알림] {alarm['time']} 알람 시작!")
    for i in range(alarm['repeat']):
        print(f"🔔 띠리리링! ({i+1}/{alarm['repeat']})")
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            os.system('echo -e "\a"')
        time.sleep((alarm['duration'] * 60) / alarm['repeat'])  # 예: 3분 5회 → 36초 간격
    print("\n알람 종료. 메뉴로 돌아갑니다. (Enter를 눌러 계속하세요)")

"""시간 형식 검증"""
def validate_time_format(alarm_time):
    try:
        datetime.strptime(alarm_time, "%H:%M")
        return True
    except ValueError:
        return False

"""알람 보기"""
def view_alarms():
    if not alarms:
        print("설정된 알람이 없습니다.")
    else:
        print("현재 설정된 알람 (시간순) :")
        for idx, alarm in enumerate(sorted(alarms, key=lambda x: x['time'])):
            print(f"  {idx+1}. {alarm['time']} | 반복 {alarm['repeat']}회, {alarm['duration']}분")

"""알람 설정"""
def set_alarm():
    try:
        # 시간 입력
        while True:
            alarm_time = input("알람 시간 입력 (HH:MM) : ").strip()
            if not validate_time_format(alarm_time):
                print("잘못된 형식입니다. 예시) 07:30")
            elif any(a['time'] == alarm_time for a in alarms):
                print("이미 등록된 알람입니다.")
            else:
                break

        # 반복 횟수 입력
        while True:
            repeat_input = input("알람 반복 횟수 입력 (예: 3) : ").strip()
            if not repeat_input.isdigit():
                print("❌ 숫자를 입력하세요.")
            else:
                repeat = int(repeat_input)
                if repeat < 1:
                    print("❌ 반복 횟수는 1 이상이어야 합니다.")
                else:
                    break

        # 울릴 시간 입력
        while True:
            duration_input = input("알람 울릴 시간 입력 (초 단위, 예: 1) : ").strip()
            if not duration_input.isdigit():
                print("❌ 숫자를 입력하세요.")
            else:
                duration = int(duration_input)
                if duration < 1:
                    print("❌ 울릴 시간은 1분 이상이어야 합니다.")
                else:
                    break

        new_alarm = {
            "time": alarm_time,
            "repeat": repeat,
            "duration": duration
        }
        alarms.append(new_alarm)
        history.append(f"설정 : {alarm_time} | 반복 {repeat}회, {duration}분간")
        print(f"[확인] 알람이 설정되었습니다 : {alarm_time}")

    except KeyboardInterrupt:
        print("\n알람 설정이 취소되었습니다.")

"""알람 삭제"""
def delete_alarm():
    view_alarms()
    if not alarms:
        return
    try:
        idx = int(input("삭제할 알람 번호 선택 : ").strip()) - 1
        if 0 <= idx < len(alarms):
            removed = alarms.pop(idx)
            history.append(f"삭제 : {removed}")
            print(f"[확인] 알람이 삭제되었습니다 : {removed}")
        else:
            print("유효하지 않은 번호입니다.")
    except ValueError:
        print("숫자를 입력하세요.")
    except KeyboardInterrupt:
        print("\n작업이 취소되었습니다.")

"""히스토리 보기"""
def view_history():
    if not history:
        print("히스토리가 없습니다.")
    else:
        print("알람 히스토리 :")
        for item in history:
            print(f" - {item}")

"""알람 확인"""
def alarm_checker():
    already_rung = set()
    while True:
        now = datetime.now().strftime("%H:%M")
        for alarm in alarms:
            if alarm['time'] == now and now not in already_rung:
                ring_alarm(alarm)
                alarms.remove(alarm)
                history.append(f"울림 : {alarm['time']}")
                already_rung.add(now)
        time.sleep(1)

"""AlarmColck"""
def main():
    show_intro()

    # 알람 체크 스레드 시작
    checker_thread = threading.Thread(target=alarm_checker, daemon=True)
    checker_thread.start()

    while True:
        show_menu()
        try:
            choice = input("메뉴 선택 (1~5) : ").strip()
            if choice not in {"1", "2", "3", "4", "5"}:
                raise ValueError
        except (ValueError, KeyboardInterrupt):
            print("유효한 번호를 입력하세요.")
            continue

        if choice == "1":
            view_alarms()
        elif choice == "2":
            set_alarm()
        elif choice == "3":
            delete_alarm()
        elif choice == "4":
            view_history()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()