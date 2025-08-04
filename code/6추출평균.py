import pandas as pd

# CSV 파일 읽기 (예: 'moisture_data.csv')
df = pd.read_csv('파일명.csv')

# 평균 컬럼 추가 (모든 행에 대해 계산)
# 모든 컬럼에 대한 평균을 만들기 위해 필요한 컬럼들 지정
moisture_cols = ['equipment_forehead_moisture', 'equipment_l_cheek_moisture', 'equipment_r_cheek_moisture', 'equipment_chin_moisture']
df['equipment_moisture_avg'] = df[moisture_cols].mean(axis=1)

# 결과 저장 (원한다면)
df.to_csv('추출값평균.csv', index=False)

# 탄력
import pandas as pd

# CSV 파일 읽기 (예: 'moisture_data.csv')
df = pd.read_csv('추출완료.csv')

# 평균 컬럼 추가 (모든 행에 대해 계산)
# 모든 컬럼에 대한 평균을 만들기 위해 필요한 컬럼들 지정
elasticity_cols = [
    '탄력_턱_R0','탄력_턱_R1','탄력_턱_R2','탄력_턱_R3','탄력_턱_R4',
    '탄력_턱_R5','탄력_턱_R6','탄력_턱_R7','탄력_턱_R8','탄력_턱_R9',
    '탄력_턱_Q0','탄력_턱_Q1','탄력_턱_Q2','탄력_턱_Q3',
    '탄력_왼쪽볼_R0','탄력_왼쪽볼_R1','탄력_왼쪽볼_R2','탄력_왼쪽볼_R3','탄력_왼쪽볼_R4',
    '탄력_왼쪽볼_R5','탄력_왼쪽볼_R6','탄력_왼쪽볼_R7','탄력_왼쪽볼_R8','탄력_왼쪽볼_R9',
    '탄력_왼쪽볼_Q0','탄력_왼쪽볼_Q1','탄력_왼쪽볼_Q2','탄력_왼쪽볼_Q3',
    '탄력_오른쪽볼_R0','탄력_오른쪽볼_R1','탄력_오른쪽볼_R2','탄력_오른쪽볼_R3','탄력_오른쪽볼_R4',
    '탄력_오른쪽볼_R5','탄력_오른쪽볼_R6','탄력_오른쪽볼_R7','탄력_오른쪽볼_R8','탄력_오른쪽볼_R9',
    '탄력_오른쪽볼_Q0','탄력_오른쪽볼_Q1','탄력_오른쪽볼_Q2','탄력_오른쪽볼_Q3',
    '탄력_이마_R0','탄력_이마_R1','탄력_이마_R2','탄력_이마_R3','탄력_이마_R4',
    '탄력_이마_R5','탄력_이마_R6','탄력_이마_R7','탄력_이마_R8','탄력_이마_R9',
    '탄력_이마_Q0','탄력_이마_Q1','탄력_이마_Q2','탄력_이마_Q3'
]
df['equipment_moisture_avg'] = df[elasticity_cols].mean(axis=1)

# 결과 저장 (원한다면)
df.to_csv('추출값평균.csv', index=False)
