from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=50, min_length=5)
    lastname: str = Field(max_length=50, min_length=2)
    email: str = Field(max_length=100, min_length=2)
    username: str = Field(max_length=250, min_length=2)
    password: str = Field(max_length=50, min_length=2)
    cohabitation_agreement: bool 
    status: int
    description: str = Field(max_length=250, min_length=0)
    knowledge_interest: str = Field(max_length=250, min_length=2)
    create_at: datetime = Field(example="2022-03-08T10:00:00")
    update_at: datetime = Field(example="2022-03-08T11:00:00")
    forgot_password: bool
    image_profile: str = Field(max_length=50, min_length=3)
    phone_number: str = Field(max_length=50, min_length=3)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "edwin",
                "lastname": "hernandez",
                "email": "edwin.jhnsn@gmail.com",
                "username": "edwinjhs",
                "password": "12345678",
                "cohabitation_agreement": "False",
                "status": 0,
                "description": "backend iasdas",
                "knowledge_interest": "conocimiento, etc",
                "create_at": "2023-03-08T15:40:10",
                "update_at": "2023-03-08T15:40:10",
                "forgot_password": "False",
                "image_profile": "../image/profile1.jpg",
                "phone_number": "3213943876"
            }
        }