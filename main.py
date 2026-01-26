def print_given(*args, **kwargs):
    for a in args:
        print(a, type(a))
    for k in sorted(kwargs):
        print(f'{k} {kwargs[k]}', type(kwargs[k]))


print_given(b=2, d=4, c=3, a=1)
print_given(1, [1, 2, 3], 'three', two=2)
