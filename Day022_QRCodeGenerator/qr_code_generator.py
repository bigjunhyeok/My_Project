import qrcode
import os
from PIL import Image

"""QR 코드 이미지 저장 디렉터리"""
OUTPUT_DIR = "QRImage"

"""인트로 출력"""
def show_intro():
    print("🔷" * 20)
    print("🔷🔷🔷🔷 QR 코드 생성기 🔷🔷🔷🔷")
    print("🔷" * 20)

"""메인 메뉴"""
def main_menu():
    user_input = input("\n📥 QR 코드에 넣을 데이터(텍스트/URL)를 입력하세요 : ")
    filename = input("💾 파일명을 입력하세요 : ").strip()

    # 확장자 없으면 .png 자동 추가
    if not filename.lower().endswith(".png"):
        filename += ".png"

    full_path = os.path.join(OUTPUT_DIR, filename)
    generate_qr_code(user_input, full_path)

"""QRCodeGenerator"""
def generate_qr_code(data: str, full_path: str):
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # QR 코드 객체 생성
    qr = qrcode.QRCode(
        version=10,  # 1~40 (높을수록 더 많은 데이터 저장 가능)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 오류 복원 수준
        box_size=10,  # 박스 크기 (픽셀)
        border=4  # 테두리 두께
    )

    qr.add_data(data)  # 데이터 추가
    qr.make(fit=True)  # 최적화된 크기로 조정

    img = qr.make_image(fill_color="black", back_color="white")  # 이미지 생성
    img.save(full_path)  # 이미지 저장
    filename = os.path.basename(full_path)
    abs_path = os.path.abspath(full_path) # 절대 경로

    print(f"\n✅ QR 코드가 '{os.path.basename(filename)}'으로 저장되었습니다.")
    print(f"📁 경로 : [{abs_path}]")

    # 이미지 자동 열기
    img.show()

if __name__ == "__main__":
    show_intro()
    main_menu()