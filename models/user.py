
"""
Represents the User database entity
"""
from argon2 import PasswordHasher
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from config import SECRET_KEY
from models.database_model import DatabaseModel, CharField


class User(DatabaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    @classmethod
    def create_user(cls, username, email, password, **kwargs):
        email = email.lower()
        try:
            cls.select().where(
                (cls.email == email) | (cls.username**username)
            ).get()
        except cls.DoesNotExist:
            user = cls(username=username, email=email)
            user.password = user.set_password(password)
            user.save()
            return user
        else:
            raise AlreadyExistsException()

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer(SECRET_KEY)
        try:
            data = serializer.loads(token)
        except (SignatureExpired, BadSignature):
            return None
        else:
            user = User.get(User.id == data['id'])
            return user

    @staticmethod
    def set_password(password):
        return PasswordHasher().hash(password)

    def verify_password(self, password):
        return PasswordHasher().verify(self.password, password)

    def generate_auth_token(self, expires=None):
        serializer = Serializer(SECRET_KEY, expires_in=expires)
        return serializer.dumps({'id': self.id})


class AlreadyExistsException(Exception):
    def __init__(self, *args, **kwargs):
        pass