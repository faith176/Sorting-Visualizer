import random


# Creates an array that counts up to the number of elements
def randomInput(elements):
    values = [(random.randrange(1,100))for i in range(elements)]
    random.shuffle(values)
    print(values)
    return values