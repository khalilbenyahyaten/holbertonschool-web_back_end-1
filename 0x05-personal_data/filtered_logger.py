#!/usr/bin/env python3

"""return the log message obfuscated"""
from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ("Name", "Address", "Email", "password", "ssn")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ generates a log"""
        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns a log message obfuscated"""
    lst = message.split(separator)

    for i in fields:
        for j in range(len(lst)):
            if lst[j].startswith(i):
                subst = i + '=' + redaction
                lst[j] = re.sub(lst[j], '', lst[j])
                lst[j] = subst
    return separator.join(lst)


def get_logger() -> logging.Logger:
    """return logging logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = RedactingFormatter(list(PII_FIELDS))
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    db = mysql.connector.connection.MySQLConnection(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return db


def main():
    """returns noth"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    logger = get_logger()
    for row in cursor:
        msg = "name={}; email={}; phone={}; ssn={}; password={};\
            ip={}; last_login={}; user_agent={}; ".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
        )
        msg = filter_datum(list(PII_FIELDS), '***', msg, '; ')
        logger.info(msg)
        cursor.close()
        db.close()
