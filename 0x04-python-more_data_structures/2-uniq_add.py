#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_val = set()
    result = sum(
        map(
            lambda x: uniq_val.add(x) or x if x not in uniq_val else 0,
            my_list))
    return result
