import json

with open('pools.json', 'r', encoding='utf-8') as inp_file:
    reader = json.load(inp_file)

filt = list(filter(lambda x: x['WorkingHoursSummer']['Понедельник'].split('-')[0] <= '10:00' and
                             x['WorkingHoursSummer']['Понедельник'].split('-')[1] >= '12:00', reader))

# 1
max_filter = max(filt, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))

# 2
# sort_filter = sorted(filt, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']),
#                      reverse=True)[0]      # можно сделать через сортировку

print(f"{max_filter['DimensionsSummer']['Length']}x{max_filter['DimensionsSummer']['Width']}")
print(max_filter['Address'])
