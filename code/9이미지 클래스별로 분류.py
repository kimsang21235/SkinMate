import os
import shutil
import pandas as pd

# 1. 경로 설정
csv_path = "파일.csv"  # 'filename'과 'class' 컬럼 포함된 CSV
base_dir = os.getcwd()          # 현재 작업 디렉토리 기준
output_dir = os.path.join(base_dir, "images")

# 2. CSV 파일 읽기
df = pd.read_csv(csv_path)

# 3. 출력 디렉토리 생성
os.makedirs(output_dir, exist_ok=True)

# 4. 파일 검색 및 moisture_class별 폴더로 복사
for idx, row in df.iterrows():
    filename = row['filename']
    class = str(row['class'])  # 폴더 이름용

    found_path = None

    # base_dir 아래 모든 파일 탐색
    for foldername, _, filenames in os.walk(base_dir):
        if filename in filenames:
            found_path = os.path.join(foldername, filename)
            break

    # 파일을 찾지 못했을 경우 경고 출력
    if not found_path:
        print(f"[WARN] {filename} 을(를) 찾지 못함")
        continue

    # moisture_class별 하위 폴더 생성
    class_folder = os.path.join(output_dir, class)
    os.makedirs(class_folder, exist_ok=True)

    # 복사 경로 설정 및 복사
    dest_path = os.path.join(class_folder, filename)
    shutil.copy2(found_path, dest_path)
    # shutil.move(found_path, dest_path)  # 이동하려면 이 줄로 교체

    print(f"[OK] {filename} → {class} 폴더 복사 완료")
