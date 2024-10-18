import random

def random_number_generator(value: int) -> str:
    random_sequence = []

    for i in range(0, value):
        i = random.randrange(0,9)
        random_sequence.append(i)
        randon_date = ''.join([str(number) for number in random_sequence])

    return randon_date
