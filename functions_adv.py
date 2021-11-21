# Function documentation strings
def myFunc(arg1, arg2=None):
    """
    myFunc(arg1, arg2=None) --> Doesn't really do anything, just prints.

    Parameters:
    arg1: pass whatever you like to print.
    arg2: second argument. Defaults to None.
    """
    print(arg1, arg2)


def addition(*args):
    sum = 0
    for arg in args: # args = [*args]
        sum += arg
    return sum

# Variable arguments list
def main_0():
    print(addition(2, 3, 4, 1))

    nums = [5, 1, 44, 89]
    nums2 = (1, 17, 3)
    nums3 = {4, 17}
    print('nums_sum:', addition(*nums))
    print('nums2_sum:', addition(*nums2))
    print('nums3_sum:', addition(*nums3))

import math

def CelsToFaren(temp):
    return (temp * 9/5) +32
def FarenToCels(temp):
    return (temp-32) * 5/9
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
# print(round_half_up(2.1175144, 4))


# Lambda functions
def main_1():
    ctemps = [0, 18, 38, 100]
    ftemps = [32, 64, 100, 212]

    # toFar = list(map(round_half_up, list(map(CelsToFaren, ctemps))))
    # toCels = list(map(round_half_up, list(map(FarenToCels, ftemps))))
    # print(toFar, toCels)

    toFars = list(map((lambda temp: round_half_up((temp * 9/5)+32)), ctemps))
    toCels = list(map((lambda temp: round_half_up((temp-32) * 5/9)), ftemps))
    print('toFars:', toFars, '\n', 'toCels:', toCels)


# keyword-only arguments
def myFunc(arg1, arg2, *, suppressExceptions=False):
    if suppressExceptions:
        print(arg1, arg2)
    else: print('Pass True')


if __name__ == '__main__':
    # print(map.__doc__)
    # print(myFunc.__doc__)
    # main_0()
    # main_1()
    myFunc(111, 'ZZZ')
    myFunc(111, 'AAA', suppressExceptions=True)