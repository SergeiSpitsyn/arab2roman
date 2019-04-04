#   I - 1
#   V - 5
#   X - 10
#   L - 50
#   C - 100
#   D - 500
#   M - 1000
#
#   39 = XXXIX
#   MCMLXXXVIII
#   MMMCMXCIX = 3999
#   CCLXXXIII = 283
#   MCMLXXXVIII = 1988
#   XCIV = 94
#   CMXCIX = 999
#   MCML = 1950
#   _________
#   правила
#   вычитания
#   IV = 4
#   IX = 9
#   XL = 40
#   XC = 90
#   CD = 400
#   CM = 900

import time

num = input('Введите целое число от 1 до 4000: ')
if num.isdigit() == True:
    print('Арабские:', num)
    num = int(num)

    if num > 0 and num <= 4000:



# Вычисление разрядов:
# Тысячи:

        cvt_tis = (num) // 1000
        cvt_sot = (num - (cvt_tis * 1000)) // 100
        cvt_des = (num - (cvt_tis * 1000) - (cvt_sot * 100)) // 10
        cvt_ed  = (num - (cvt_tis * 1000) - (cvt_sot * 100) - (cvt_des * 10)) // 1

        print('Тысячи:  ', cvt_tis)
        print('Сотни:   ', cvt_sot)
        print('Десятки: ', cvt_des)
        print('Единицы: ', cvt_ed)
        print()

# Поскольку римская система счисления условно кратна 5-ти (1, 5, 10, 50, ...),
# будем последовательно сравнивать каждый разряд с числом 5.
# Разряд единиц в числе может быть от 0 до 9, поэтому:
# 1 Если разряд_единиц > 5, то возможны два случая:
#       a) (x - 5) > 3, где x - количество единиц; тогда
#          по правилам вычитания "забираем" из разряда
#          десятков одну единицу так, чтобы получилось IX;
#       б) (x - 5) <= 3, тогда
#          умножаем символ 'I' на количество единиц и пишем справа от
#          символа 'V', например VII.
# 2 Если разряд_единиц <= 5, то возможны два случая:
#       а) (5 - x) > 3, тогда
#          по правилам вычитания "забираем" из пятёрки
#          одну единицу так, чтобы получилось IV (пишем I слева от V);
#       б) (5 - x) <= 3, тогда
#          умножаем символ 'I' на количество единиц и пишем, например II.
#
#
#


        # Данный IF реализует модуль разности количества тысяч и числа 5
        if cvt_tis <= 4:    
                itog = ('M' * cvt_tis)


        # Данный IF реализует модуль разности количества сотен и числа 5
        if cvt_sot > 5:    
            dif_sot = cvt_sot - 5
            if dif_sot > 3:
                itog = itog + ('C' * (dif_sot - 3) + 'M')
            else:
                itog = itog + ('D' + 'C' * dif_sot)
        elif cvt_sot <= 5:
            dif_sot = 5 - cvt_sot
            if cvt_sot > 3:
                itog = itog + ('C' * dif_sot + 'D')
            else:
                itog = itog + ('C' * cvt_sot)


        # Данный IF реализует модуль разности количества десятков и числа 5
        if cvt_des > 5:    
            dif_des = cvt_des - 5
            if dif_des > 3:
                itog = itog + ('X' * (dif_des - 3) + 'C')
            else:
                itog = itog + ('L' + 'X' * dif_des)
        elif cvt_des <= 5:
            dif_des = 5 - cvt_des
            if cvt_des > 3:
                itog = itog + ('X' * dif_des + 'L')
            else:
                itog = itog + ('X' * cvt_des)        


        # Данный IF реализует модуль разности количества единиц и числа 5
        # |5 - x|, где x - количество единиц:
        if cvt_ed > 5:    
            dif_ed = cvt_ed - 5
            if dif_ed > 3:
                itog = itog + ('I' * (dif_ed - 3) + 'X')
            else:
                itog = itog + ('V' + 'I' * dif_ed)
        elif cvt_ed <= 5:
            dif_ed = 5 - cvt_ed
            if cvt_ed > 3:
                itog = itog + ('I' * dif_ed + 'V')
            else:
                itog = itog + ('I' * cvt_ed)

        print('Римские: ', itog)

    elif num < 1:
        print('Вводимое число должно быть положительным')

    elif num > 4000:
        print('Вводимое число не должно превышать 4000')

else:
    print('Ошибка ввода числа')
    print('Попробуйте ещё раз')
    

time.sleep(6)
