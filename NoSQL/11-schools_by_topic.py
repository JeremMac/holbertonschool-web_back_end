#!/usr/bin/env python3
'''
A module that define the schools_by_topic function.
'''


def schools_by_topic(mongo_collection, topic):
    '''
     A Python function that returns the list of
     school having a specific topic.

     Returns a list of specifics topics.
    '''
    school_topics = mongo_collection.find({"topics": topic})
    My_list = list(school_topics)
    return My_list
