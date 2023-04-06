import hashlib


class User:
    def __init__(self):
        # Basic info
        self.username: str = ""
        self.password: str = ""
        self.balance: int = 0

        # In System
        self.mobile_plan_id: int = 0

        # In Web
        self.domain_name: str = ""
        self.domain_ip: str = ""
        self.current_vpn_plan_id: int = 0
        self.current_vps_plan_id: int = 0



    def encrypt_password(self, password: str) -> str:
        """Only use when creating a new user"""
        return str(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000))

    def is_valid_password(self, password: str) -> bool:
        """Only use when logging in"""
        password = self.encrypt_password(password)
        return self.password == password

    def get_username(self):
        return self.username

    def serialize(self) -> dict[str, str | int]:
        # `: dict[str, str | int]`: a dictionary with keys are strings and values are either strings or integers
        return {
            # Basic info
            "username": self.username,
            "password": self.password,
            "balance": self.balance,

            # In System
            "mobile_plan_id": self.mobile_plan_id,

            # In Web
            "domain_name": self.domain_name,
            "domain_ip": self.domain_ip,
            "current_vpn_plan_id": self.current_vpn_plan_id,
            "current_vps_plan_id": self.current_vps_plan_id,
        }
    
