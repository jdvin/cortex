array = [[1,2,3,4],['a','b','c','d']]

def get_index(item):
    if type(item) == int or type(item) == str:
        return index(item)
    else:
        get_index(item)

for i in array:
    print(get_index(i))