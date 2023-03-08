from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(plain_password: str) -> str:
        return password_context.hash(plain_password)

    @staticmethod
    def verify(plain_password: str, hashed_pass: str) -> bool:
        return password_context.verify(plain_password, hashed_pass)

