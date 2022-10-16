money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05
month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

while salary + money_capital - spend >= 0:
    money_capital = salary + money_capital - spend
    spend = spend * increase
    month += 1

print(month)

# ответ, выдаваемый EduTools = 3, но это неверно, даже если считать вручную
# поскольку через 3 месяца у нас на руках будет еще 7700 остатка от подушки