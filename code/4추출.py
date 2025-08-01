import pandas as pd
import os

# 현재 경로의 CSV 파일 읽기
csv_path = os.path.join(os.getcwd(), "정면.csv")
df = pd.read_csv(csv_path)

# 'Moisture'가 포함된 컬럼 이름들 추출
moisture_columns = [col for col in df.columns if '추출할 단어' in col]

# 'info_filename' 컬럼 추가
selected_columns = ['info_filename'] + moisture_columns

# 해당 컬럼만 추출
df_selected = df[selected_columns]

# 결과 저장
df_selected.to_csv("추출완료.csv", index=False, encoding="utf-8-sig")

print("✅ 'info_filename' + 'Moisture' 포함 컬럼 추출 완료!")
