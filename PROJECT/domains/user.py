import hashlib

class User:
    def __init__(self, username: str, password: str, balance: float = 0, product_id=None , current_plan=None , current_domain=None , current_service=None , current_VPN=None):
        self.username = username
        self.password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), b'salt', 100000)
        self.balance = balance
        self.current_plan = current_plan
        self.product_id = product_id
        self.current_domain = current_domain
        self.current_service = current_service
        self.current_VPN = current_VPN
        


    def check_password(self, password):
        return self.password == hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), b'salt', 100000)

    def get_username(self):
        return self.username