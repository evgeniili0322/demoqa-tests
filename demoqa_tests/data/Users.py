import dataclasses


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: int
    date_of_birth: {}
    subject: str
    hobby: str
    picture: str

