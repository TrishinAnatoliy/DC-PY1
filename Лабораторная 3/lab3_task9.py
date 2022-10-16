salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 1.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
n = 1
# TODO Оформить решение
while n <= 10:
    need_money = need_money + spend - salary
    spend = spend * increase
    n = n + 1
print(round(need_money))
