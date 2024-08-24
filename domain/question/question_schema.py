import datetime

from pydantic import BaseModel

# 질문 스키마
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime