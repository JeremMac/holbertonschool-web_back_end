#!/usr/bin/env python3
'''
A module that define
'''


def update_topics(mongo_collection, name, topics):
    '''
    A Python function that changes all topics of
    a school document based on the name.

    Returns: nothing.
    '''
    update_data = mongo_collection.update_many({"name": name},
                                               {"$set": {"topics": topics}})
