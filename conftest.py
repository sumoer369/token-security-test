import pytest
import requests

def pytest_html_report_title(report):
    report.title = "Token权限矩阵与撤销回归测试报告"

@pytest.fixture(autouse=True)
def reset_mock_server():
    try:
        requests.post("http://127.0.0.1:5000/api/test/reset", timeout=1)
    except Exception:
        pass
    yield