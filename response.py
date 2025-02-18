from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Route để lấy danh sách người dùng từ API
@app.route('/users', methods=['GET'])
def get_users():
    url = "https://demo-rest-api-ewdl.onrender.com/users"  # API từ server khác
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        return jsonify(users)
    else:
        return jsonify({"error": "Lỗi khi lấy dữ liệu!", "status_code": response.status_code}), response.status_code

# Route mặc định
@app.route('/')
def home():
    return "API đang chạy! Truy cập /users để lấy danh sách người dùng."

# Chạy Flask server khi chạy file trực tiếp
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
