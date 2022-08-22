from ninja import Schema
from pydantic import Field, EmailStr #validate the email

class AccountIn(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    password1: str = Field(min_length = 8)
    password2: str = Field(min_length = 8)

class details(Schema):
    detail: str

class TokenOut(Schema):
    access: str

class AccountOut(Schema):
    first_name: str
    last_name: str
    email: EmailStr

class AuthOut(Schema):
    token: TokenOut
    account: AccountOut

class SigninIn(Schema):
    email: EmailStr
    password: str