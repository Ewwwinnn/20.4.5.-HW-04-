import json

with open('orders_july_2023.json', 'r') as f:
    orders = json.load(f)

expensive_order = ""
expensive_price = 0
biggest_order = ""
biggest_quantity = 0
busy_day = ""
busy_day_count = 0
active_user = ""
active_user_count = 0
rich_user = ""
rich_user_total = 0
sum_of_orders = 0
sum_of_items = 0

busy_days = {}
users = {}
rich_users = {}

for order_id, order_data in orders.items():
    date = order_data["date"][:10]
    user_id = order_data["user_id"]
    quantity = order_data["quantity"]
    price = order_data["price"]

    if price > expensive_price:
        expensive_order = order_id
        expensive_price = price

    if quantity > biggest_quantity:
        biggest_order = order_id
        biggest_quantity = quantity

    if date not in busy_days:
        busy_days[date] = 1
    else:
        busy_days[date] += 1

    if user_id not in users:
        users[user_id] = 1
    else:
        users[user_id] += 1

    if user_id not in rich_users:
        rich_users[user_id] = price
    else:
        rich_users[user_id] += price

    sum_of_orders += price

    sum_of_items += quantity

for day, count in busy_days.items():
    if count > busy_day_count:
        busy_day = day
        busy_day_count = count

for user, count in users.items():
    if count > active_user_count:
        active_user = user
        active_user_count = count

for user, total in rich_users.items():
    if total > rich_user_total:
        rich_user = user
        rich_user_total = total

avg_order = sum_of_orders / len(orders)
avg_item = sum_of_orders / sum_of_items

print(f"Номер самого дорого заказа за июль: {expensive_order}, стоимость заказа: {expensive_price}")
print(f"Номер заказа с наибольшим количеством товаров: {biggest_order}, количество товаров: {biggest_quantity}")
print(f"День с наибольшим количеством заказов в июле: {busy_day}, количество заказов: {busy_day_count}")
print(f"Пользователь с наибольшим количеством заказов за июль: {active_user}, количество заказов: {active_user_count}")
print(f"Пользователь с наибольшей общей стоимостью заказов за июль: {rich_user}, общая стоимость заказов: {rich_user_total}")
print(f"Средняя стоимость заказа в июле: {avg_order:.2f}")
print(f"Средняя стоимость одного товара в июле: {avg_item:.2f}")