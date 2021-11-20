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
        print(m) 

    for i,m in enumerate(zip(days, daysLt), start=1):
        print(i, '-', m[0], '=', m[1], 'in Lt')

if __name__ == '__main__':
    # main_0()
    main_1()