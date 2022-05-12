from datetime import datetime
from app.bs_storm.core.database import Base
from sqlalchemy import Table,Column,VARCHAR,BIGINT,INT,BLOB,DATETIME,ForeignKey,TEXT,Enum
from sqlalchemy.orm import relationship,backref
from app.bs_storm.utils.repr import repr_create
import enum


class ActionStatus(enum.Enum):
    Error = "Error",
    Pulling = "Pulling",
    Success = "Success",
    Change = "Change",
    Execute = "Execute"

class RunningStatus(enum.Enum):
    Green = "Green",
    Blue = "Blue"

class Api(Base):

    __tablename__ = 'api'
    __table_args__ = {'extend_existing': True}

    API_NAME = Column(VARCHAR(50),primary_key=True)
    API_INDEX = Column(TEXT(),nullable=True)
    API_NGINX_DOMAIN = Column(VARCHAR(50),nullable=False)
    API_BLUE_PORT = Column(INT(),nullable=False)
    API_GREEN_PORT = Column(INT(), nullable=False)
    API_RUNNING_STATUS = Column(Enum(RunningStatus),nullable=False)

    def __repr__(self):
        return repr_create("Api",["API_NAME","API_INDEX","API_NGINX_DOMAIN","API_BLUE_PORT","API_GREEN_PORT","API_RUNNING_STATUS"]).format(self=self)

class Actions(Base):

    __tablename__ = 'actions'
    __table_args__ = {'extend_existing': True}

    ACTION_PK = Column(INT(),primary_key=True)
    ACTION_STATUS = Column(Enum(ActionStatus),nullable=False)
    ACTION_START_TIME = Column(DATETIME(),nullable=True)
    ACTION_END_TIME = Column(DATETIME(), nullable=True)
    Api_API_NAME = Column(VARCHAR(50), ForeignKey("api.API_NAME"),nullable=False)

    api = relationship("Api", backref=backref("Actions"))

    def __repr__(self):
        return repr_create("Action",["ACTION_PK","ACTION_STATUS","ACTION_START_TIME","ACTION_END_TIME","API_API_NAME"]).format(self=self)