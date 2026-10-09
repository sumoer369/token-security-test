import requests

BASE_URL = "http://127.0.0.1:5000"

def test_revoke_token():
    requests.post(f"{BASE_URL}/api/test/reset")
    revoke_res = requests.post(f"{BASE_URL}/api/token/revoke", json={"token": "write_token"})
    assert revoke_res.status_code == 200

    response = requests.post(
        f"{BASE_URL}/api/order/update",
        headers={"Authorization": "Bearer write_token"}
    )
    assert response.status_code == 401
    print("Token撤销回归测试通过！")