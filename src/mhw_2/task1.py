"""task1.
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров. 
Пример: 
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета. 
Output: Общая цена 9 рублей 60 копеек
"""

rub = int(input('Введите стоимость в рублях:'))
kop = int(input('Введите стоимость в копейках:'))
kol = int(input('Введите количество товара:'))
result: float = (kop / 100 + rub) * kol
v_rub = int(result // 1)
v_kop = round(result % 1 * 100)
print('Стоимость ', kol, ' товаров равна: ', v_rub, ' рублей ', v_kop, ' копеек.')
