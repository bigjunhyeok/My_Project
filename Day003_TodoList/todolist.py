import json
import os
from datetime import datetime

TODOLIST_FILE = "my_to_do_list.json"


""" todolist 불러오기 """
def load_file():
    if os.path.exists(TODOLIST_FILE):
        with open(TODOLIST_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"tasks_list": [], "completed_tasks_list": []}

""" todolist 저장하기 """
def save_file(tasks):
    with open(TODOLIST_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

""" task 목록 출력 """
def list_tasks():
    tasks = load_file()
    if not tasks["tasks_list"]:
        print("작업 목록이 없음.")
    else:
        for i, task in enumerate(tasks["tasks_list"]):
            print(f"{i}. {task}")

""" 완료된 task 목록 출력 """
def completed_list_tasks():
    tasks = load_file()
    if not tasks["completed_tasks_list"]:
        print("완료된 작업 목록이 없음.")
    else:
        for i, task in enumerate(tasks["completed_tasks_list"]):
            print(f"{i}. {task}")

""" task 추가 """
def add_task(task):
    tasks = load_file()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks["tasks_list"].append({"task": task, "timestamp": timestamp})
    save_file(tasks)
    print(f"[+] 추가완료. : {task}")

""" task 제거 """
def remove_task(index):
    tasks = load_file()
    if not tasks["tasks_list"]:
        print("삭제할 목록이 없음.")
    else:
        try:
            removed = tasks["tasks_list"].pop(index)
            save_file(tasks)
            print(f"[-] 제거완료. : {removed}")
        except IndexError:
            print("유효하지 않은 번호.")

""" task 완료 처리 """
def complete_task(index):
    tasks = load_file()
    if not tasks["tasks_list"]:
        print("완료할 목록이 없음.")
    else:
        try:
            completed = tasks["tasks_list"].pop(index)
            tasks["completed_tasks_list"].append(completed)
            save_file(tasks)
            print(f"[✔] 완료됨. : {completed}")
        except IndexError:
            print("유효하지 않은 번호.")

""" 모든 task 완료 처리 """
def complete_all_task():
    tasks = load_file()
    if not tasks["tasks_list"]:
        print("완료할 목록이 없음.")
    else:
        try:
            tasks["completed_tasks_list"].extend(tasks["tasks_list"])   # 전체 이동
            tasks["tasks_list"].clear() # 기존 목록 초기화
            save_file(tasks)
            print(f"[✔] 완료됨.")
        except IndexError:
            print("유효하지 않은 번호.")

""" task 목록 초기화 """
def clear_task_list():
    confirm = input("모든 [task 목록]을 초기화하시겠습니까? (y/n) : ").strip().lower()
    if confirm in ["y", "yes"]:
        tasks = load_file()
        tasks["tasks_list"] = []
        save_file(tasks)
        print("모든 [task 목록] 초기화 완료.")
    else:
        print("초기화 취소.")

""" completed task 목록 초기화 """
def clear_completed_task_list():
    confirm = input("모든 [completed_task 목록]을 초기화하시겠습니까? (y/n) : ").strip().lower()
    if confirm in ["y", "yes"]:
        tasks = load_file()
        tasks["completed_tasks_list"] = []
        save_file(tasks)
        print("모든 [completed_task 목록] 초기화 완료.")
    else:
        print("초기화 취소.")

""" 도움말 출력 """
def show_help():
    print("\n############### 명령어 도움말 ###############")
    print("list                 - 작업 목록 출력")
    print("completed_list       - 완료된 작업 목록 출력")
    print("add                  - 작업 추가")
    print("remove               - 작업 제거 (번호 입력 필요)")
    print("complete             - 작업 완료 처리 (번호 입력 필요)")
    print("complete_all         - 작업 목록 일괄 완료 처리")
    print("clear_task           - 작업 목록 초기화")
    print("clear_completed_task - 완료된 작업 목록 초기화")
    print("help                 - 명령어 도움말 출력")
    print("exit                 - 프로그램 종료")
    print("#############################################\n")

""" to-do-list """
def main():
    while True:
        command = input("\n 명령 입력 (list/completed_list/add/remove/complete/complete_all/clear_task/clear_completed_task/help/exit) : ").strip().lower()
        if command == "list":
            list_tasks()
        elif command == "completed_list":
            completed_list_tasks()
        elif command == "add":
            task = input("추가할 task : ")
            add_task(task)
        elif command == "remove":
            index = int(input("삭제할 tasks 번호 : "))
            remove_task(index)
        elif command == "complete":
            index = int(input("완료할 tasks 번호 : "))
            complete_task(index)
        elif command == "complete_all":
            complete_all_task()
        elif command == "clear_task":
            clear_task_list()
        elif command == "clear_completed_task":
            clear_completed_task_list()
        elif command == "help":
            show_help()
        elif command == "exit":
            print("프로그램 종료.")
            break
        else:
            print("유효하지 않은 명령.")

if __name__ == "__main__":
    main()