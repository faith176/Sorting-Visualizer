import random


# Creates an array that counts up to the number of elements
def ascInput(elements):
    values = [i + 1 for i in range(elements)]
    random.shuffle(values)
    print(values)
    return values
