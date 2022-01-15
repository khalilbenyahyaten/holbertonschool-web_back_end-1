#!/usr/bin/env python3
""" List all documents module """


def insert_school(mongo_collection, **kwargs):
    """ List all documents """
    return mongo_collection.insert_one(kwargs).inserted_id or None
