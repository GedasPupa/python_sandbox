import itertools

# any() all() min() max() sum() sorted() .sort(reverse=True) 
def main_0():
    list1 = [1, -2, 3, 0, 8, 4]
    # any()
    print(any(list1))
    # all()
    print(all(list1))
    # min() and max()
    print(min(list1), max(list1))
    # sum()
    print(sum(list1))
    # sorted() // .sort()
    print('sorted(list1, reverse=True):', sorted(list1, reverse=True))    # nekeičia orignalaus list'o, grąžina surušiuotą
    list2 = list(list1)
    list2.sort()            # keičia originalų ir nieko negrąžina (None)
    print('original list1:', list1)
    print('original list2 [after list2.sort()]:', list2)


# iter() next() enumerate() zip()
def main_1():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sut", "Sun"]
    daysLt = ["Pir", "Ant", "Tre", "Ket", "Pen", "Št", "Sk"]

    # iter() and next() // nesamoniu prirasiau - i panagrinejau:
    i = iter(days)
    for rng in range(8):
        print(i.__length_hint__())
        print(next(i))
        if i.__length_hint__() == 0:
            days.append("EigthDay")
            break
    print(days)

    # iterate using a function and a sentinel
    with open('lines_file.txt', 'r') as f_r:
        for line in iter(f_r.readline, ''): # or just stop at '' - empty string - the end of file
            # print(line)
            pass

    # regular iteration in daysLt
    for indx in range(len(daysLt)):
        print(indx+1, daysLt[indx])

    # using enumerate() reduces code and provides counter
    for ind,m in enumerate(days, start=1):
        print(ind, m)

    # using zip() to combine sequences
    daysLt.append('AštuntaDienis') 
    daysLt.append('9dienis')
    for m in zip(days, daysLt): # zip() terminates then the shortes seq is exhausted
        print('zip(two, seqs):', m) 

    for i,m in enumerate(zip(days, daysLt), start=1):
        print(i, '-', m[0], '=', m[1], 'in Lt')


# filter() map()
def main_2():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = 'AbhkETdpLwZzoqwgJRe'
    grades = (71, 89, 55, 98, 65, 86, 90, 91, 88, 95)

    def toGrades(x):
        if x > 90:
            return 'A'
        elif x > 80:
            return 'B'
        elif x > 70:
            return 'C'
        elif x > 60:
            return 'D'
        else: 
            return 'E'

    # filter()
    odds = list(filter(lambda x: x%2 != 0, nums))
    evens = list(filter(lambda x: x%2 == 0, nums))
    print(odds, '\n', evens)

    lowers = list(filter(lambda x: x.islower(), chars))
    uppers = list(filter(lambda x: x.isupper(), chars))
    print(lowers, '\r\n', uppers)

    # map()
    squares = list(map(lambda x: x**2, grades))
    print(squares)

    letterGrades = list(map(toGrades, sorted(grades, reverse=True)))
    print(letterGrades)


# itertools: cycle() count()
def main_3():
    seq1 = ['Jons', 'Petrs', 'Antans']

    # cycle()
    cycle1 = itertools.cycle(seq1)
    for rng in range(4): print(next(cycle1))
    # count()
    count1 = itertools.count(100, 10)
    for rng in range(5): print(next(count1))
    # accumulate()
    vals = [10, 30, 10, 40, 30, 50, 20]
    acc1 = list(itertools.accumulate(vals))
    acc2 = list(itertools.accumulate(vals, max))
    print(acc1, '\n', acc2)
    # chain()
    chained = list(itertools.chain(seq1, 'XXX'))
    print(chained)
    # dropwhile() takewhile()
    print(list(itertools.dropwhile(lambda x: x<40, vals)))
    print(list(itertools.takewhile(lambda x: x<40, vals)))


if __name__ == '__main__':
    # main_0()
    main_1()
    # main_2()
    # main_3()