import pandas as pd

df = pd.read_csv('파일명.csv')
result_df = df[['info_filename', '추출할내용_mean']]
result_df.to_csv('평균값.csv', index=False)