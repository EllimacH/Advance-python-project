import time
import hashlib
from datetime import datetime
date = datetime.now()
products = [200000, 150000, 100000, 50000]
times = [20, 15, 10, 5]
months = [1, 1, 1, 1]
balance = 0
attempts = 0
usernames = []
passwords = []


def create_account():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password2 = input("Reconfirm your password: ")
    if password == password2:
        usernames.append(username)
        passwords.append(password)
        print("Account created successfully!\n")
    else:
        print("Invalid information! Please try again.\n")


def sign_in():
    global attempts
    username = input("Nhập tên người dùng: ")
    password = input("Nhập mật khẩu: ")
    if username == "phong" and password == "1234":
        print("Đăng nhập thành công!")
        print("[+] Ngày:", date.strftime("%d-%m-%Y %I:%M"))
    else:
        print("Sai tên người dùng hoặc mật khẩu!")
        attempts += 1
        if attempts == 2:
            print("Đăng nhập sai quá 10 lần!")
            exit()


def deposit():
    global balance
    amount = int(input("Nhập số tiền cần nạp: "))
    balance += amount
    print("Nạp tiền thành công! Số dư hiện tại là: ", balance)
    print("[+] Ngày:", date.strftime("%d-%m-%Y %I:%M"))


def withdraw():
    global balance
    amount = int(input("Nhập số tiền cần rút: "))
    if amount > balance:
        print("Số dư không đủ!")
    else:
        balance -= amount
        print("Rút tiền thành công! Số dư hiện tại là: ", balance)
        print("[+] Ngày:", date.strftime("%d-%m-%Y %I:%M"))


def check_balance():
    global balance
    print("Số dư hiện tại của bạn là: ", balance)


def check_product():
    global products
    print("Danh sách sản phẩm:")
    for i in range(len(products)):
        print(i+1, "- Giá: ", products[i], "VND", "Thời gian: ",
              times[i], "phút", "Thời hạn: ", months[i], "tháng")


def buy_product():
    global balance
    product_id = int(input("Nhập Mã sản phẩm muốn mua: "))
    if product_id == 1:
        price = products[0]
    elif product_id == 2:
        price = products[1]
    elif product_id == 3:
        price = products[2]
    else:
        print("Không tìm thấy sản phẩm này!")
        buy_product()
    if price > balance:
        print("Số dư không đủ để mua sản phẩm này!")
    else:
        balance -= price
        print("Mua sản phẩm thành công! Số dư hiện tại là: ", balance)
        print("[+] Ngày:", date.strftime("%d-%m-%Y %I:%M"))


print("Xin chào!")
while True:
    choice = int(input("Vui lòng lựa chọn một trong những tính năng sau: \n1. Tạo tài khoản mới \n2. Đăng nhập \n3. Nạp tiền \n4. Rút tiền \n5. Kiểm tra số dư \n6. Xem sản phẩm \n7. Mua sản phẩm \n8. Thoát \n"))
    if choice == 1:
        create_account()
    elif choice == 2:
        sign_in()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        check_balance()
    elif choice == 6:
        check_product()
    elif choice == 7:
        buy_product()
    elif choice == 8:
        print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi!")
        print("[+] Ngày:", date.strftime("%d-%m-%Y %I:%M"))
        break
    else:
        print("Vui lòng chọn tính năng hợp lệ!")