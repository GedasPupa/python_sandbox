import string
import collections
from collections import defaultdict
from collections import Counter
from collections import OrderedDict

# namedtuple - Tuple with named fields
# OrderedDict, defaultdict - Dictionaries with special properties
# Counter - Counts distinct values
# deque - Double-ended list object

# namedtuple
def main_0():
    Point = collections.namedtuple('Point', 'x y')
    myPoint = Point(10, 20)
    print(myPoint, myPoint.x, myPoint.y)
    print(myPoint.x * myPoint.y)

    # _replace() for creation of a new instance:
    myPoint = myPoint._replace(x=100)
    print(myPoint.x * myPoint.y)
    # print(myPoint._make())

# defaultdict
def main_1():
    fruits = ['apple', 'banana', 'orange', 'pear',
              'apple', 'grape', 'banana', 'banana']
    
    fruitCounter = {}
    fruitCounter_dd = defaultdict(lambda: 1000)
    # fruitCounter_dd = defaultdict(int) # starts from 0


    for f in fruits:
        if f in fruitCounter.keys():
            fruitCounter[f] += 1
        else:
            fruitCounter[f] = 1

    for fr in fruits:
        fruitCounter_dd[fr] += 1

    print(fruitCounter)
    print(fruitCounter_dd.items())
    for k,v in fruitCounter_dd.items():
        print(k + ': ' + str(v))


# Counter
def main_2():
    class1 = ['Bob', 'John', 'Anna', 'John', 'Bob', 'Bob', 'Petras']
    class2 = ['Jonas', 'Petras', 'Antanas', 'Jonas', 'Anna']

    c1 = Counter(class1)
    c2 = Counter(class2)

    # how many Bobs in class1?
    print(c1['Bob'])

    # how many students in class1?
    print(sum(c1.values()), ' - students in class1')

    # combine two classes
    c1.update(class2)
    print(sum(c1.values()), ' - students in c1 [Counter!] combined')

    # most_common() - c1.update(class2) - works from line 62
    print(c1.most_common(3))

    # separate the classes (counters) again:
    c1.subtract(class2)
    print(c1.most_common(3))

    # what's common between two classes:
    print (c1 & c2)


# OrderedDict
def main_3():
    # list of teams with wins and losses
    sportsTeams = [('Dragons', (12, 15)), ('Rockets', (11, 19)),
                   ('Kings', (21,7)), ('Warriors', (18, 10))]
    
    teamsSorted = sorted(sportsTeams, key=lambda k: k[1][0], reverse=True) #sorted by wins
    # print(sorted(sportsTeams, key=lambda t: t[1][1], reverse=True)) # sorted by losses
    print(teamsSorted)

    teams = OrderedDict(teamsSorted)
    print(teams)

    # popitem() - remove the top/bottom item
    tm, wl = teams.popitem(False)
    print('Top team:', tm, wl)
    tm1, wl1 = teams.popitem() # default = popitem(True)
    print('Bottom team: ', tm1, wl1)
    print(teams)

    # test for equality
    a = OrderedDict({'a': 1, 'c': 3, 'b': 2})
    b = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    print('Equality test:', a == b)


# Deque - double-ended queue
# appendleft() - append() / popleft() - pop() / rotate(param: howManyToRotate?[default=1])
def main_4():
    d = collections.deque(string.ascii_lowercase)
    # print('string.ascii_lowecase:', string.ascii_lowercase)
    print('Item count:', str(len(d)))
    # for el in d:
    #     print(el.upper(), end=',')

    d.popleft()
    d.pop()
    d.appendleft('1')
    d.append('9')
    # for el in d:
    #     print(el, end='.')

    # rotate()
    print(d)
    d.rotate(5)
    d.rotate(-6)
    print(d)



if __name__ == '__main__':
    # main_0()
    # main_1()
    # main_2()
    # main_3()
    main_4()