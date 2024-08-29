from sqlalchemy.orm import Session

from models import Question


def get_question_list(db: Session):
    _question_list = (db.query(Question)
                      .order_by(Question.create_date.desc())  # 최신 질문순
                      .all())
    return _question_list


def get_question(db: Session, question_id: int):
    question = db.get(Question, question_id)
    return question
