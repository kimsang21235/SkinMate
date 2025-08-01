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
