"""프로그램 종료 요청"""
def check_exit(value):
    # 사용자가 'q' 입력 시 프로그램 종료
    if value.lower() == 'q':
        print("계산기 종료.")
        exit()

"""숫자 유효성 검사"""
def check_number(input_number):
    # 유효한 숫자가 입력될 때까지 반복해서 입력받음
    while True:
        try:
            value = input(input_number)
            check_exit(value)  # 종료 요청 확인
            return float(value)  # 숫자로 변환 후 반환
        except ValueError:
            print("올바르지 않은 숫자.")

"""연산자 유효성 검사"""
def check_oper():
    # 유효한 연산자가 입력될 때까지 반복해서 입력받음
    valuid_operators = ('+', '-', '*', '/', '%')

    while True:
        operator = input("연산자 입력 (+, -, *, /, %) : ")
        check_exit(operator)  # 종료 요청 확인

        if operator in valuid_operators:
            return operator  # 유효한 연산자라면 반환
        print("올바르지 않은 연산자.")

"""계산기"""
def calculate():
    # 기본 사칙연산 계산기 수행
    print("기본 계산기 (종료: 'q')")
    while True:
        num1 = check_number("첫 번째 숫자 입력: ")
        operator = check_oper() # 연산자 유효성 검사
        num2 = check_number("두 번째 숫자 입력: ")

        # 연산 수행
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("0으로 나눌 수 없음.")
                continue
            result = num1 / num2
        elif operator == '%':
            if num2 == 0:
                print("0으로 나눌 수 없음.")
                continue
            result = num1 % num2

        # 결과 출력
        print(f"결과: {num1} {operator} {num2} = {result}")

# 실행
if __name__ == "__main__":
    calculate()