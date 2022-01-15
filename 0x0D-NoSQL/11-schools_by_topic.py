#!/usr/bin/env python3
""" List all documents module """


def schools_by_topic(mongo_collection, topic):
    """ List all documents """
    return mongo_collection.find(
        {'topics': topic},
    )
