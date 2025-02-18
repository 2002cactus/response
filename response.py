import requests

# API endpoint để lấy danh sách user
url = "https://demo-rest-api-ewdl.onrender.com/users"  # Địa chỉ server Flask đang chạy

# Gửi yêu cầu GET để lấy danh sách người dùng
response = requests.get(url)

# Kiểm tra phản hồi từ server
if response.status_code == 200:
    users = response.json()
    if users:
        print("\n✅ Đã nhập thông tin thành công! Danh sách người dùng:")
        for idx, user in enumerate(users, start=1):
            print(f"{idx}. {user['name']} - {user['email']}")
    else:
        print("\n⚠️ Chưa có dữ liệu nào được nhập!")
else:
    print("\n❌ Lỗi khi lấy dữ liệu! Mã lỗi:", response.status_code)
