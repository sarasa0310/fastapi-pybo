from sqlalchemy.orm import Session

from models import Question


def get_question_list(db: Session):
    _question_list = (db.query(Question)
                      .order_by(Question.create_date.desc())
                      .all())
    return _question_list