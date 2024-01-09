#!/usr/bin/env python3


'''
A module that defines the list_all function.
'''

def list_all(mongo_collection):
    '''
    A Python function that lists all documents in a collection.

    Returns: a list of the document in
    mongo_colection otherwise returns an empty
    list.
    '''
    My_list = mongo_collection.find()
    result_list = list(My_list)
    return result_list
