def main_0():
    def FahrenheitToCelsius(t):
            return (t-32) * 5/9

    print ( list( map( FahrenheitToCelsius, [32, 65, 104, 212] ) ) )
    # or just:
    print( [ (t-32)*5/9 for t in [32, 65, 104, 212] ] )


# list comprehensions
def main_1():
    evens = [2,4,6,8,10,12,14,16,18,20]

    evenSquared = list(map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens)))
    evenSquared2 = [ e**2 for e in filter(lambda e: e>4 and e<16, evens) ]
    evenSquared3 = [ e**2 for e in evens if e>4 and e<16 ]

    print(evenSquared, evenSquared2, evenSquared3)

# dictionary comprehension
def main_2():
    ctemps = [0, 12, 34, 100]

    tempDict = { t: (t*9/5)+32 for t in ctemps if t<100 }
    print(tempDict)
    print(tempDict[12])

    team1 = {"Jones": 18, "James": 24, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    # merging two dicts with comprehension:
    newTeam = { k:v for team in (team1, team2) for k,v in team.items() } # if v < 58
    print(newTeam)

# set comprehensions
def main_3():
    ctemps = [0, 5, 12, 34, 100, 5, 34]
    ftempsList = [ (t*9/5)+32 for t in ctemps ]
    ftempsSet = { (t*9/5)+32 for t in ctemps }
    print(ftempsList, '\n', ftempsSet)

    tempStr = "The quick brown fox jumped over the lazy dog"
    chars = { c.upper() for c in tempStr if not c.isspace() }  # if c != ' '
    print(chars)


if __name__ == '__main__':
    # main_0()
    # main_1()
    # main_2()
    main_3()