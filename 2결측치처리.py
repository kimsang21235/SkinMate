import pandas as pd
import os

# 현재 경로 기준
csv_path = os.path.join(os.getcwd(), "final_flattened_equipment.csv")

# CSV 불러오기
df = pd.read_csv(csv_path)

# 빈값을 0으로 채우기
df.fillna(0, inplace=True)

df.to_csv("final_flattened_equipment_filled.csv", index=False, encoding="utf-8-sig")  # 새 파일로 저장

print("✅ 빈값을 0으로 채운 CSV 저장 완료!")
