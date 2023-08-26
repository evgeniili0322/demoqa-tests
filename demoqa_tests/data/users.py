import dataclasses
from datetime import datetime
from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth: datetime
    subject: str
    hobby: str
    picture: str
    current_address: str
    state: str
    city: str


@dataclasses.dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str
