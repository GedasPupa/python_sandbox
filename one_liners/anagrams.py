is_anagram = lambda x, y: sorted(x) == sorted(y)
print(is_anagram('elvis', 'lives'))
print(is_anagram('eelvis', 'elives'))
print(is_anagram('elvis', 'dead'))
