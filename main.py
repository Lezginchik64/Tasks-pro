import sys
from datetime import datetime

# 1
d = [datetime.strptime(i.strip(), '%Y-%m-%d') for i in sys.stdin]
print((max(d) - min(d)).days)

# 2
dates = [datetime.fromisoformat(line.strip()) for line in sys.stdin]
print((max(dates) - min(dates)).days)
