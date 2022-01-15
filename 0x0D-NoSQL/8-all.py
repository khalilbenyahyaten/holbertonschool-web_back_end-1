#!/usr/bin/env python3
""" List all documents module """


def list_all(mongo_collection):
    """ List all documents """
    return mongo_collection.find() or []
