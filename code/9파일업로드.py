import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('파일.csv')

# filename 컬럼 수정
df['filename'] = df.apply(lambda row: f"gs://cgp-moisture-test/extracted_images/{row['class']}/{row['filename']}", axis=1)

# 결과 확인 (선택)
print(df.head())

# 필요한 경우 저장
df.to_csv('결과.csv', index=False)
