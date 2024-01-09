#!/usr/bin/env python3


'''
A module that defines the insert_school function.
'''


def insert_school(mongo_collection, **kwargs):
    '''
    A Python function that inserts a new document
    in a collection based on kwargs.

    Returns the new inserted id.
    '''
    insert_data = mongo_collection.insert_one(kwargs)
    return insert_data.inserted_id