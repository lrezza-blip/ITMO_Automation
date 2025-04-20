# #проверяем является ли число положительным или отрицательным и выводит сообщение
# num = 4
#
# # if num >= 0:
# #     print ('число больше либо равно 0')
# # else:
# #     print('число отрицательное')
# #
# # #str_2 содержит str_1?
# # def task_yes_no(str_1,str_2):
# #     if str_1 in str_2:
# #         print ('ДА')
# #     else:
# #         print('НЕТ')
# #
# # task_yes_no(str_1 = 'test',str_2 = 'test1')
# #
# # num_float = 0
# #
# # if num_float > 0:
# #     print ('положительное число')
# # elif num_float == 0:
# #     print('Ноль')
# # else:
# #     print('отрицательное число')
#
#
# permit_print = True
#
# if num > 0 and permit_print:
#     print('num - отрицательное')
# elif not permit_print:
#     print('печать запрещена')
from selectors import SelectSelector


# def a(year):
#     if year in range (1,5):
#         print('бак')
#     elif year in range (5,7):
#         print('маг')
#     elif year in range (7,9):
#         print('аспирин')
#     else:
#         print('введите год')
#
# a(10)

num = 1
if num>100 or num<-100:
    print ('-')
else:
    print ('+')