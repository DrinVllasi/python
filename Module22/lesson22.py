from pydantic import BaseModel , conint , constr
from typing import Optional

# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str

# user = User(id=1,name='john',age=25,email='john@gmail.com')
# print(user)

class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

user1 = User(id=1,name='john',age=25,email='john@gmail.com')
print(user1)

user2 = User(id=1,name='john',age=25)
print(user2)

user3 = User(id=1,name='john',email='john@gmail.com')
print(user3)

user4 = User(id=1,name='john')
print(user4)

class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2,max_length=20)

valid_user = another_user(id=1,name="drin")
print(valid_user)

unvalid_user = another_user(id=0,name="d") #the id is not greater than 1 so it sends an error and the name isnt atleast 2 characters long so it send an error aswell
print(unvalid_user)

