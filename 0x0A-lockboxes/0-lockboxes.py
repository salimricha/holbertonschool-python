#!/usr/bin/python3
def canUnlockAll(boxes):

    opened = [False for i in range(len(boxes))]
    opened[0] = True
    used = [False for i in range(len(boxes))]
    checkopened = [True for i in range(len(boxes))]

    found = True
    while(if found is True):
        found = False
        for i in range(len(boxes)):
            if opened[i] is True and used[i] is False:
                used[i] = True
                found = True
                for key in boxes[i]:
                    try:
                        opened[key] = True
                    except:
                        pass
    if opened == checkopened:
        return True
    else:
        return False
