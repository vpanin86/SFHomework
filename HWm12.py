per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_list = list(per_cent.values())
money_input = float(input("Введите сумму вклада в рублях:\n"))
def take_percent (number):  #Функция для вычисления заработка на проценте по вкладу
    return number*money_input*0.01
deposit = list(map(take_percent, per_cent_list))
print (deposit)
print ('Максимальная сумма, которую вы можете заработать:', max(deposit), 'рублей')
