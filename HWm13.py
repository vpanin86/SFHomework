count = int(input("Введите желаемое количество билетов "))
discount = 0.1
age_list = []
price_list = []
# Счет количества зрителей и запись возраста каждого из них
for i in range(count):
    print("Введите возраст", i+1, "-го зрителя ")
    age_list.append(int(input()))
# Определение цены билета в зависимости от возраста
for i in range(count):
    if age_list[i] < 18:
        price_list.append(0)
    elif 25 > age_list[i] >= 18:
        price_list.append(990)
    elif age_list[i] >= 25:
        price_list.append(1390)
# Вычисление суммы за все билеты
if count > 3:
    print("Сумма заказа, руб (с учетом скидки)")
    print(float(sum(price_list[:])) - sum(price_list[:])*discount)
else:
    print("Сумма заказа, руб")
    print(float(sum(price_list[:])))
