from pydantic import BaseModel, FieldSerializationInfo, field_validator, conint,constr

class User(BaseModel):
    id: int
    name: str
    age: int

    @field_validator('age')
    def age_must_be_positive(cls, v, info:FieldSerializationInfo):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v
try:
    user = User(id=1,name="joe",age=-1)
    print(user)
except ValueError as e:
    print(e)

class Address(BaseModel):
    street: str
    city: str

class Users(BaseModel):
    id: int
    name: str
    address: Address