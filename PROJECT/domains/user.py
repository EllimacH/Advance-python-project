import hashlib

class User:
    def __init__(self, username, password, balance=0, current_plan=None):
        self.username = username
        self.password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), b'salt', 100000)
        self.balance = balance
        self.current_plan = current_plan

    def check_password(self, password):
        return self.password == hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), b'salt', 100000)
