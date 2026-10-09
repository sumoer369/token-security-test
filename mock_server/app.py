from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_TOKENS = {
    "readonly_token": {"role": "readonly"},
    "write_token": {"role": "write"},
    "publish_token": {"role": "publish"}
}

REVOKED_TOKENS = set()

def check_token(required_role):
    auth_header = request.headers.get("Authorization", "")
    token = auth_header.replace("Bearer ", "")
    if token in REVOKED_TOKENS:
        return jsonify({"msg": "Token 已撤销"}), 401
    if token not in VALID_TOKENS:
        return jsonify({"msg": "非法 Token"}), 401
    if VALID_TOKENS[token]["role"] != required_role:
        return jsonify({"msg": "权限不足"}), 403
    return None

@app.route("/api/order/query", methods=["GET"])
def query_order():
    error = check_token("readonly")
    if error:
        return error
    return jsonify({"data": "订单查询成功", "role": "readonly"}), 200

@app.route("/api/order/update", methods=["POST"])
def update_order():
    error = check_token("write")
    if error:
        return error
    return jsonify({"data": "订单修改成功", "role": "write"}), 200

@app.route("/api/package/publish", methods=["POST"])
def publish_package():
    error = check_token("publish")
    if error:
        return error
    return jsonify({"data": "发布包已生成", "role": "publish"}), 200

@app.route("/api/token/revoke", methods=["POST"])
def revoke_token():
    data = request.get_json()
    token_to_revoke = data.get("token")
    if token_to_revoke:
        REVOKED_TOKENS.add(token_to_revoke)
        return jsonify({"msg": f"Token {token_to_revoke} 已撤销"}), 200
    return jsonify({"msg": "请求参数错误"}), 400

@app.route("/api/test/reset", methods=["POST"])
def reset():
    REVOKED_TOKENS.clear()
    return jsonify({"msg": "重置成功"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)