# # типы данных
#
# 5 6 #целые числа int
# "yess" # строка str string
# [0, 1, 2, 3, 4] # список из 5 переменных list
# [5, 4, 'jhke' 'yhjhji'] # список из двух чисел и двух строк
#
# {
#     'hell': 1,
#     'paradise': 0
# } # словарь dict dictionary
# 4.5 # числа с плавающей точкой float
# True 1 False 0 #булевые значения bool
#
# # перевод между типами данных
#
# str(10) # из числа в строку
#
# int("10") # из строки в число
#
# # из целого в вещественное
# float(5)
# int(5.6)# из вещественного в целое
#
# # из bool в string
# str(True)
# # из string в bool
# bool("True")

i = 0
ich = "5"
print(i + int(ich))

def pluss(a, b):
    result = a + b
    return result

result = pluss(5, 10)