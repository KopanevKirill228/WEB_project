import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Asks(SqlAlchemyBase):
    __tablename__ = 'asks'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    ask = sqlalchemy.Column(sqlalchemy.String, nullable=True)
