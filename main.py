from datetime import datetime, timedelta

pattern, day = '%d.%m.%Y', timedelta(days=1)
data = datetime.strptime(input(), pattern)
print((data - day).strftime(pattern))
print((data + day).strftime(pattern))
