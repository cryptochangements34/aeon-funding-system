from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

import settings


def create_session():
    from funding.orm.orm import base
    engine = sa.create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False, encoding="latin")
    session_factory = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)
    session = scoped_session(session_factory)
    base.query = session.query_property()
    base.metadata.create_all(bind=engine)
    return session
