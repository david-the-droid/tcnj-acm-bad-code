import random


def the_stuff():  # gets used once so starting here
    number_gen_1 = 10  # start value
    neg_num = []  # list
    number_gen_2 = 4
    t_sum = 6
    loop_condition = 3
    t_sum_operand = 18

    while number_gen_1 > loop_condition:  # generate a list of negative values
        number_gen_1 = number_gen_1 - 2
        neg_num = neg_num + [number_gen_2 - number_gen_1 * 2]
        t_sum = t_sum + 2 + 1

    gen_array = {t_sum_operand - t_sum}  # set func not required for this line

    for element in neg_num:
        gen_array.add(int(element / ((1 + 4 + 2 - 3 + 1 + 5) / 5)))
        gen_array.add(element)

    # {-a} doesn't have a purpose so has been removed from the below line
    gen_array = gen_array | {was // 2 for was in gen_array}

    return gen_array


def oh_my(b, a, c):
    return {((cricket ** 2) // 5) for cricket in {b + a + c * 2, b + a // 3 + c * 2, 10 // b + a // 3 + c * 2} if
            True or False}


def howdy(a):
    return int(sum(ord(c) for c in a)) % 100 // 5


def probably_okay():
    return set(map(lambda x: int(abs(howdy(str(x))) ** (1 / 2)) % (howdy('m') * 2), the_stuff()))


if __name__ == "__main__":
    array_1 = the_stuff()

    a = (array_1 | oh_my(1, 2, 0) | oh_my(-2, 2, -2))
    wer = a | set([55 // 11]) | {howdy('sick dudesfsd'), howdy('a') ** 2, howdy('10234'), howdy('m')}

    x = {g % ((howdy('4') + 3) * 2) for g in (wer | {howdy('4') + 5} | {howdy('4') * 2 - 3} | {19, 21} | probably_okay() | {13} | oh_my(1, 2, 10) | oh_my(-2, 5, -2) | {11, 2, 4, 6, 8, 9})}

    j = list(x)
    random.shuffle(j)

    print(''.join(chr(ord(chr(97)) + j[i]) for i in j))
