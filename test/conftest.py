import os
import pytest
from app.bs_storm.utils.log import logger
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.bs_storm.main import app
import dotenv
from app.bs_storm.core.database import get_db, Base
import pymysql

dotenv.load_dotenv()
tmp_api_info = {
        "API_NAME": "hos",
        "API_INDEX": "this is shit game. oh my mistake. IS NOT GAME",
        "API_NGINX_DOMAIN": "sigong.ubuntu.bs_storm.xyz",
        "API_BLUE_PORT": "65",
        "API_GREEN_PORT": "6565",
        "API_RUNNING_STATUS": "green"
    }


@pytest.fixture
def fastapi_client():

    fastapi_client = TestClient(app)
    return fastapi_client


@pytest.fixture
def tmp_db():
    logger.debug("start test db set up......")

    #test db table create
    logger.debug("create test table......")
    pymysql.install_as_MySQLdb()
    test_db_conn = pymysql.connect(host=os.environ['DB_HOST'],user=os.environ['DB_USER'],password=os.environ['DB_PASSWD'])
    cursor = test_db_conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS `{os.environ['DB_NAME']}-test`")
    sql = open("test_bg_storm.sql",encoding="utf-8").read().replace("\n","")
    cursor.execute(sql)

    cursor.fetchall()
    cursor.close()

    logger.debug("create test table success!")
    logger.debug("make test database session")

    TEST_DB_CONN_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        os.environ['DB_USER'],
        os.environ['DB_PASSWD'],
        os.environ['DB_HOST'],
        os.environ['DB_PORT'],
        os.environ['DB_NAME']+"-test",
    )
    print(TEST_DB_CONN_URL)
    db_engine = create_engine(TEST_DB_CONN_URL)
    db_session = sessionmaker(bind=db_engine, autoflush=False, autocommit=False)

    def get_db():
        try:
            db = db_session()
            yield db

        finally:
            db.close()

    tmp_db = get_db()
    logger.debug("make test database set up fin.")
    return tmp_db

@pytest.fixture(autouse=True)
def setup():
    pass

@pytest.fixture(autouse=True)
def teardown():
    yield
    logger.debug("clean test data base...")

    pymysql.install_as_MySQLdb()
    test_db_conn = pymysql.connect(host=os.environ['DB_HOST'],user=os.environ['DB_USER'],password=os.environ['DB_PASSWD'],charset="utf8mb4")
    cursor = test_db_conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS `{os.environ['DB_NAME']}-test`")

    cursor.fetchall()
    cursor.close()

    logger.exception("clean test data base fin")