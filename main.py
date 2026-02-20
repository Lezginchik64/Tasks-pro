import sys
from datetime import datetime

dates = [datetime.strptime(i.strip(), '%d.%m.%Y') for i in sys.stdin if i != '\n']

if sorted(set(dates)) == dates:
    print("ASC")
elif sorted(set(dates), reverse=True) == dates:
    print("DESC")
else:
    print("MIX")
