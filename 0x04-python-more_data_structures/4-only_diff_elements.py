#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set(
        filter(
            lambda x: x not in set_2, set_1)) | set(
                filter(
                    lambda x: x not in set_1, set_2))
    return diff_set
