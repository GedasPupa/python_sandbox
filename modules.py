# A Module is basically a file containing a set of functions to include in your application.
# There are core Python modules, modules you can install using pip package manager
# (including Django) as well as custom modules.

# Core module e.g.:
import datetime
today = datetime.date.today()
time = datetime.datetime.now().time()
print(today)
print(time)

# or importing just {date} from datetime:
from datetime import date
today2 = date.today()
print(f'Today2: {today2}')

# Pip module
from camelcase import CamelCase
c = CamelCase()
print(c.hump('hello there world'))

# Custom module
from validator import validate_email

email = 'ggg#ggg.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is invalid')