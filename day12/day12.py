import json


def iterate(obj):
    suma = 0
    if isinstance(obj, dict):
        for key in obj:
            # part 2
            if key == 'red' or obj[key] == 'red':
                return suma
        for i in obj:
            suma += iterate(obj[i])
    elif isinstance(obj, list):
        for i in obj:
            suma += iterate(i)
    elif isinstance(obj, int):
        return obj
    else:
        return 0
    return suma


son = open("day12.txt").read()

son = json.loads(son)

print(iterate(son))
