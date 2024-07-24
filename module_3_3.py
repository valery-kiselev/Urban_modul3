def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#1st program
print_params()
print_params(b = 'слово', c = not True)
print_params(b = 25)#Переменные в Python имеют динамическую типизацию
print_params(c = [1,2,3])#тип данных переменной определяется во время выполнения на основе типа присвоенного ей значения

#2nd program
values_list = [2, 'слово', False]
values_dict = {'a':1, 'b':'строка', 'c':True}
print_params(*values_list)
print_params(**values_dict)

#3st program
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)