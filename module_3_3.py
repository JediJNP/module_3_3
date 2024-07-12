print('Распаковка')
print('----------')

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = (1, True, 'seven')
values_dict = {'a':7, 'b':8, 'c':9}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = (7, 'seven')
print_params(*values_list_2, 42)