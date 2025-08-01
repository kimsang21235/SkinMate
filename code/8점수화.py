import pandas as pd
import numpy as np

df = pd.read_csv('파일명.csv')

bins = [30, 41, 45, 50, 55, 60, 65, 70, 75, 94]  # 9개 구간 + 구간은 전체 범위에서 적당히 나눌 수 있게 설정
labels = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5] # 구간 별 레이블 설정
# 구간 별 레이블 컬럼 생성 + 평균값을 이용한 클래스화
df['moisture_class'] = pd.cut(df['moisture_mean'], bins=bins, labels=labels, right=False)

# 각 클래스당 개수 확인
counts = df['moisture_class'].value_counts().sort_index()
print(counts)

# 각 클래스당 개수 괜찮으면 csv 파일로 저장
a_df = df[['info_filename', 'moisture_class']]
a_df['moisture_class'].value_counts()
a_df.to_csv('수분점수.csv', index=False)

