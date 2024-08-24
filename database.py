from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URL = 'sqlite:///./myapi.db'

# 커넥션 풀(데이터베이스 접속 객체 풀) 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
# 데이터베이스에 접속하기 위해 필요한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델을 구성할 때 사용되는 클래스
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
