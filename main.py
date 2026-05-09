from enum import StrEnum
from pydantic import BaseModel


class ContactType(StrEnum):
    EMAIL = "email"
    PHONE = "phone"


class ContactInfo(BaseModel):
    name: str
    contact_type: ContactType


if __name__ == "__main__": 
    contact_info = ContactInfo(name="erek", contact_type=ContactType.EMAIL)

    from rich.pretty import pprint

    pprint(contact_info)