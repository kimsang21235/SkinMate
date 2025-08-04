import pandas as pd

# CSV 파일 읽기 (예: 'moisture_data.csv')
df = pd.read_csv('파일명.csv')

# 평균 컬럼 추가 (모든 행에 대해 계산)
# 모든 컬럼에 대한 평균을 만들기 위해 필요한 컬럼들 지정
moisture_cols = ['equipment_forehead_moisture', 'equipment_l_cheek_moisture', 'equipment_r_cheek_moisture', 'equipment_chin_moisture']
df['equipment_moisture_avg'] = df[moisture_cols].mean(axis=1)

# 결과 저장 (원한다면)
df.to_csv('추출값평균.csv', index=False)
