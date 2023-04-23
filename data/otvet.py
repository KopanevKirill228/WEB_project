import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Otvet(SqlAlchemyBase):
    __tablename__ = 'otvet'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    otvet = sqlalchemy.Column(sqlalchemy.String, nullable=True)
