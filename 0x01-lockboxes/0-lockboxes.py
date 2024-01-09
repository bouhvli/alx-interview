#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
        There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    if not boxes:
        return False

    number_of_boxes = len(boxes)
    boxes_unlocked = set()
    keys_to_check = [0]

    boxes_unlocked.add(0)
    while keys_to_check:
        box = keys_to_check.pop()
        for key in boxes[box]:
            if key not in boxes_unlocked and number_of_boxes > key >= 0:
                boxes_unlocked.add(key)
                keys_to_check.append(key)
    return number_of_boxes == len(boxes_unlocked)
