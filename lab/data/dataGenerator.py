import random as rand

def random_stimulation(size, sparcity):
    stim_pattern = [0 for i in range(size)]
    for i in range(int(sparcity * size)):
        _flag = False
        while not _flag:
            _index = rand.randint(0, size-1)
            if stim_pattern[_index] == 0:
                stim_pattern[_index] = 1
                _flag = True

    return stim_pattern

