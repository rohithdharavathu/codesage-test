from typing import Optional


class UserService:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id: int) -> Optional[dict]:
        return self.db.query(user_id)

    def validate_user(self, user_id: int) -> bool:
        user = self.get_user(user_id)
        return user is not None


class TokenService:
    def __init__(self, secret: str):
        self.secret = secret

    def generate_token(self, user_id: int) -> str:
        return f"{self.secret}:{user_id}"

    def verify_token(self, token: str) -> bool:
        return token.startswith(self.secret)


def authenticate(username: str, password: str) -> bool:
    service = UserService(db=None)
    return service.validate_user(user_id=1)

def validate_user(self, user_id: int) -> bool:
    user = self.get_user(user_id)
    if user is None:
        return False
    return user.get("active", False)  # changed behavior
# new changes 

def validate_user(self, user_id: int) -> bool:
    user = self.get_user(user_id)
    if user is None:
        return False
    return user.get("active", False)

    
# def validate_user(self, user_id: int) -> bool:
#     user = self.get_user(user_id)
#     if user is None:
#         return False
#     return user.get("active", False) -> testing
# updated
