import os
import pytest
import requests
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "permission_cases.yaml")

def load_cases():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 重点在这行：把 case_name 作为用例的 ID
@pytest.mark.parametrize("case", load_cases())
def test_permission_matrix(case):
    url = f"http://127.0.0.1:5000{case['endpoint']}"
    headers = {}
    if case.get("token"):
        headers["Authorization"] = f"Bearer {case['token']}"

    if case["method"] == "GET":
        response = requests.get(url, headers=headers)
    else:
        response = requests.post(url, headers=headers)

    print(f"执行用例: {case['case_name']} -> 状态码: {response.status_code}")
    assert response.status_code == case["expected_status"]