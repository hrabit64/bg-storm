from os import environ

from dotenv.main import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# .env 환경파일 로드
load_dotenv()

# 디비 접속 URL
DB_CONN_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    environ['DB_USER'],
    environ['DB_PASSWD'],
    environ['DB_HOST'],
    environ['DB_PORT'],
    environ['DB_NAME'],
)
# 모델 초기화를 위한 db 커넥션 부분
db_engine = create_engine(DB_CONN_URL)
db_session = sessionmaker(bind=db_engine,autoflush=False,autocommit=False)
Base.metadata.create_all(db_engine,checkfirst=True)


def get_db():
    try:
        db = db_session()
        yield db

    finally:
        db.close()
