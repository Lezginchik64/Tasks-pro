from datetime import datetime, timedelta

pattern = '%H:%M'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)

while True:
    end_lesson = start + timedelta(minutes=45)
    if end_lesson > end:
        break
    print(f'{start.strftime(pattern)} - {end_lesson.strftime(pattern)}')
    start = end_lesson + timedelta(minutes=10)
