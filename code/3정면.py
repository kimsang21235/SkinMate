import pandas as pd
import os

# 현재 경로 기준 CSV 불러오기
csv_path = os.path.join(os.getcwd(), "파일명.csv")
df = pd.read_csv(csv_path)

# 'info_filename' 컬럼에 'F'가 포함된 행만 남김
df_filtered = df[df['info_filename'].str.contains('F', na=False)]

# 결과 저장
df_filtered.to_csv("정면.csv", index=False, encoding="utf-8-sig")

print("✅ 'F'가 포함된 행만 필터링 완료!")
-----------------------------------------------------------------------
# 사진 파일 정면 사진만 남기고 나머지 삭제
import os

base_dir = os.getcwd()  # 현재 작업 디렉터리

for foldername, subfolders, filenames in os.walk(base_dir):
    # 현재 탐색 중인 폴더명이 4자리 숫자인 경우만 처리
    folder_basename = os.path.basename(foldername)
    if folder_basename.isdigit() and len(folder_basename) == 4:
        for filename in filenames:
            if (("_L" in filename) or ("_R" in filename)) and filename.endswith(".jpg"):
                file_path = os.path.join(foldername, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
