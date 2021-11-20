def main_old():
    print('MAIN_OLD:')
    name = 'Brad'
    age = 39

    # Concatenate
    # print('Hello my name is ' + name + ' and I am ' + str(age) + '.')

    # Arguments by position
    # print('Hello my name is {nnaammee} and I am {age} years old.'.format(nnaammee=name, age=age))

    # F-Strings (3.6+)
    print(f'Hello my name is {name} and I am {age} y.o. - not too old for learning Python! :)')

    #  String methods

    alpha = 'aabBBBCccZ'
    s = '123333helloworlD'
    n = '11101'

    print(s.capitalize())
    print('find(\'o\')', s.find('o'))
    print('count(\'l\'): ', s.count('l'))
    print('length of s: ', len(s))
    print('islower()???', s.islower())
    print('is alpha numeric?', s.isalnum())
    print('isalpha()? ', alpha.isalpha())
    print('endwith(\'a\')', s.endswith('a'))
    print('isdigit()', n.isdigit())
    print('split(): ', s.split())
    print('rsplit(): ', s.rsplit())
    print(s.replace('123', 'Hello hello, '))


### Strings vs. bytes

def main_0():
    print('MAIN_0:')

    # define some starting values
    b = bytes([0x41,0x42,0x43,0x44])
    print(b)

    s = 'This is a string'
    print(s)

    # combining:
    print(b.decode('utf-8') + ' ' + s)
    print(b + ' '.encode('utf-8') + s.encode('utf-8'))

    # utf-32
    # print('s-32:', s.encode('utf-32'))


### Template strings

from string import Template

def main_1():
    print('MAIN_1:')

    # using .format():
    str = 'Šiuo metu mokausi {0} ir žiūriu {1}!'.format('Advanced Python', 'Paskaitą')
    print(str)

    # template with placeholders:
    templ = Template('Šiuo metu mokausi ${mokausi} ir žiūriu ${paskaita}!')

    # substitute method with keyword args
    str2 = templ.substitute(mokausi='labai labai advanced PY', paskaita='paskaitą tiesiai iš LI')
    print(str2)

    # substitute method with dictionary
    data = {
        "mokausi": "labai labai advanced PY",
        "paskaita": "paskaitą tiesiai tiesiai iš LI"
    }
    print(templ.substitute(data))

if __name__ == '__main__':
    # main_old()
    # main_0()
    main_1()