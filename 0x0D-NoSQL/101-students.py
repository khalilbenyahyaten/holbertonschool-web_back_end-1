#!/usr/bin/env python3
""" List all documents module """
import pymongo


def top_students(mongo_collection):
    """ List all documents """
    return mongo_collection.aggregate(
        {
            "$unwind": {
                "path": "$topics",
                "preserveNullAndEmptyArrays": "true"
            }
        }, {
            "$group": {
                "_id": "$_id",
                "Atef": {
                    "$topics.score"
                }
            }
        }
    )
