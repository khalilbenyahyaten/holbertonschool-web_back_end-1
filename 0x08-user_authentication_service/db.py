#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:

    def __init__(self):
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add_user"""
        from user import User

        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """find user"""
        results = self._session.query(User).filter_by(**kwargs)
        return results.one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """update user"""
        DBSession = self._session

        user = self._session.query(User).filter_by(id=user_id).one()
        for key, value in kwargs.items():
            if hasattr(user, key) is False:
                raise ValueError
            setattr(user, key, value)
        DBSession.commit()
