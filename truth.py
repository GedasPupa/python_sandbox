if not(() or [] or {} or 0 or 0.0 or '' or False or None or set() or range(0)):
    print('All - False')
else:
    print('Not all..')

class myClass:
    # def __bool__(self): # False
    #     return False

    def __len__(self):  # False
        return 0

    # pass

obj1 = myClass()
print(bool(obj1))