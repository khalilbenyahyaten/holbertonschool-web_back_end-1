#!/usr/bin/env python3
""" List all documents module """
from pymongo import MongoClient

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

client = MongoClient("mongodb://127.0.0.1:27017")
nginx_collection = client.logs.nginx

print("{} logs".format(nginx_collection.count()))
print("Methods:")

for method in methods:
    print("\t method {}: {}".format(
        method,
        nginx_collection.count(
                {"method": method}
            )
    ))

print("{} status check".format(
        nginx_collection.count(
                {
                    "method": "GET",
                    "path": "/status"
                }
            )
    )
)
