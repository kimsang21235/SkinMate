import pandas as pd

# CSV 파일 불러오기 (파일명은 실제 파일명으로 변경)
df = pd.read_csv('moisture_with_filename.csv')

# 'info_filename' 기준으로 그룹화하고, 각 moisture 컬럼들은 합산(또는 최대값 등 원하는 집계 함수 사용)
df_agg = df.groupby('info_filename').agg({
    # 합산할 컬럼들로 변경
    'equipment_forehead_moisture': 'sum',
    'equipment_l_cheek_moisture': 'sum',
    'equipment_r_cheek_moisture': 'sum',
    'equipment_chin_moisture': 'sum',
}).reset_index()
df_agg.to_csv("추출값모음.csv", index=False, encoding="utf-8-sig")
