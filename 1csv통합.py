import os
import json
import pandas as pd
import ast

root_dir = os.getcwd()
all_data = []

def parse_equipment(equipment_field):
    """
    equipment 필드를 문자열로 받아도, 리스트든 dict든 상관없이 통일적으로 dict로 병합
    """
    if isinstance(equipment_field, str):
        try:
            parsed = ast.literal_eval(equipment_field)  # 문자열을 리스트/딕셔너리로 파싱
        except Exception:
            return {}
    else:
        parsed = equipment_field

    if isinstance(parsed, list):
        merged = {}
        for item in parsed:
            if isinstance(item, dict):
                merged.update(item)
        return merged
    elif isinstance(parsed, dict):
        return parsed
    else:
        return {}

# JSON 로딩
for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".json"):
            json_path = os.path.join(subdir, file)
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_data.extend(data)
                    elif isinstance(data, dict):
                        all_data.append(data)
            except Exception as e:
                print(f"❌ 오류 {json_path}: {e}")

df_raw = pd.DataFrame(all_data)

# equipment 필드 정리 (핵심)
if "equipment" in df_raw.columns:
    df_raw["equipment"] = df_raw["equipment"].apply(parse_equipment)

# dict형 컬럼들 평탄화
df_final = pd.DataFrame()
for col in df_raw.columns:
    if df_raw[col].apply(lambda x: isinstance(x, dict)).all():
        expanded = pd.json_normalize(df_raw[col])
        expanded.columns = [f"{col}_{subcol}" for subcol in expanded.columns]
        df_final = pd.concat([df_final, expanded], axis=1)
    else:
        df_final[col] = df_raw[col]

# 저장
output_path = os.path.join(root_dir, "final_flattened_equipment.csv")
df_final.to_csv(output_path, index=False, encoding="utf-8-sig")
print(f"✅ 저장 완료: {output_path}")
