price_for_vacation = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
total_toys = number_puzzles + number_dolls + \
             number_teddy_bears + number_minions + number_trucks

# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.

total_sum = number_puzzles * 2.60 + number_dolls * 3 + number_teddy_bears * 4.10 + \
            number_minions * 8.20 + number_trucks * 2


if total_toys >= 50:
    discount_25 = 0.25 * total_sum
    int(discount_25)
    final_price = total_sum - discount_25
    rent = 0.1 * final_price
    profit = final_price - rent
    money_left = profit - price_for_vacation
elif total_toys < 50:
    rent = 0.1 * total_sum
    profit = total_sum - rent

final_price = total_sum - discount_25
rent = 0.1 * final_price
profit = final_price - rent
money_left = profit - price_for_vacation

if profit > price_for_vacation:
    print(f"Yes! {money_left} lv left.")
else:
    print(f"Not enough money! {money_left} lv needed.")