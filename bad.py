"""
Description: Program to generate a random sequence of numbers which is outputted as the revelant characters of the
alphabet
"""


import random


def the_stuff() -> set:  # gets used once so starting here
    """
    Function generates a list of integers containing values equal to or less than zero
    :return:
    """
    number_gen_1 = 10
    number_gen_2 = 4
    t_sum = 6
    loop_condition = 3
    t_sum_operand = 18
    neg_num = []        # stores initial negative numbers generated
    floor_list = []     # stores the floored floating values

    while number_gen_1 > loop_condition:  # generate a list of negative values
        number_gen_1 = number_gen_1 - 2
        neg_num = neg_num + [number_gen_2 - number_gen_1 * 2]
        t_sum = t_sum + 2 + 1

    gen_set = {t_sum_operand - t_sum}  # set func not required for this line

    for element in neg_num:
        gen_set.add(int(element/2))
        gen_set.add(element)

    for element in gen_set:
        val = element // 2  # floor divide e.g 5//2 = 2.00 although python treats this as "2" in a set
        floor_list.append(val)

    gen_set = gen_set | set(floor_list)

    return gen_set


def oh_my(num_1: int, num_2: int, num_3: int) -> set:
    """
    Function generates a list of numbers based on input and defined set calculation
    :param num_1:
    :param num_2:
    :param num_3:
    :return: set
    """

    defined_set = {num_1 + num_2 + num_3 * 2, num_1 + num_2 // 3 + num_3 * 2, 10 // num_1 + num_2 // 3 + num_3 * 2}
    cricket_set = []

    for cricket in defined_set:
        cricket_val = cricket ** 2 // 5
        cricket_set.append(cricket_val)

    if num_2 > num_1 and num_2 > num_3:  # reverse list
        cricket_set.reverse()

    if num_1 > num_2 and num_1 > num_3:  # swap first two elements
        copy_1 = cricket_set[0]
        copy_2 = cricket_set[1]
        cricket_set[0] = copy_2
        cricket_set[1] = copy_1

    if num_3 > num_2 and num_3 > num_1:  # reverse and swap last two elements
        cricket_set.reverse()
        copy_1 = cricket_set[1]
        copy_2 = cricket_set[2]

        cricket_set[1] = copy_2
        cricket_set[2] = copy_1

    cricket_set = set(cricket_set)

    print(cricket_set)

    return cricket_set

    # nope
    # return {((cricket ** 2) // 5) for cricket in {num_1 + num_2 + num_3 * 2, num_1 + num_2 // 3 + num_3 * 2, 10 // num_1 + num_2 // 3 + num_3 * 2} if True
    #  or False}


def howdy(str_1: str) -> int:
    """
    :param str_1: Input string
    :return: Returns a modulo floor sum of all the ascii characters in a string e.g "a" -> str_1 -> gives "97"
    """

    # ord returns the number representing the unicode code of a specified character
    # for loop sums ord values
    # then % 100 // 5 is performed

    sum_val = 0
    for element in str_1:
        sum_val += ord(element)

    modulo_floor_sum = sum_val % 100 //5

    return modulo_floor_sum


def probably_okay():
    return set(map(lambda x: int(abs(howdy(str(x))) ** (1 / 2)) % (howdy('m') * 2), the_stuff()))


#  keeping changes to what is effectively is a demo program to a minimum
if __name__ == "__main__":

    set_1 = the_stuff()
    set_2 = oh_my(1, 2, 0)
    set_3 = oh_my(-2, 2, -2)

    combined_sets = (set_1 | set_2 | set_3)

    print(type(howdy('sick dudesfsd')))

    wer = combined_sets | {[55 // 11]} | {howdy('sick dudesfsd'), howdy('a') ** 2, howdy('10234'), howdy('m')}

    x = {g % ((howdy('4') + 3) * 2) for g in (wer | {howdy('4') + 5} | {howdy('4') * 2 - 3} | {19, 21} | probably_okay() | {13} | oh_my(1, 2, 10) | oh_my(-2, 5, -2) | {11, 2, 4, 6, 8, 9})}

    alphabet_number_list = list(x)
    random.shuffle(alphabet_number_list)

    print(''.join(chr(ord(chr(97)) + alphabet_number_list[index]) for index in alphabet_number_list))
