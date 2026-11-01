# Online Python compiler (interpreter)
# Write and run Python online using this editor.

Veg_sandwich = 60
Masala_dosa = 80
chole_rice = 90
paneer_role = 100
Tea = 20
print("======== SMART CANTEEN=========")
print("1.Veg_sandwich - 60")
print("2.Masala_dosa - 80")
print("3.chole_rice - 90")
print("4.paneer_roll - 100")
print("5.Tea - 20\n")
order_items = []
while True:
    add_item = int(input("\nadd your item:-"))
    add_quantity = int(input("add your quantity:-"))
    if add_item == 1:
        item_name = "Veg sandwich"
        item_price = Veg_sandwich
    elif add_item == 2:
        item_name = "Masala dosa"
        item_price = Masala_dosa
    elif add_item == 3:
        item_name = "chole rice"
        item_price = chole_rice
    elif add_item == 4:
        item_name = "paneer roll"
        item_price = paneer_role
    elif add_item == 5:
        item_name = "Tea"
        item_price = Tea
    else:
        print("Invalid item number.")
        continue

    line_cost = item_price * add_quantity
    order_items.append((item_name, add_quantity, line_cost))
    print(f"Added: {item_name} X {add_quantity} = Rs {line_cost}")
    another_item = input("do you want to add another item?(y/n)")
    if another_item.lower() == 'n':
       break
print("\n=======RECEIPT========")
if len(order_items) == 0:
    print("No order was placed.")
else:
    subtotal = 0

    for item in order_items:
        item_name = item[0]
        quantity = item[1]
        line_cost = item[2]
        subtotal += line_cost
        print(f"{item_name} x {quantity}: Rs.{line_cost:.2f}")

    if subtotal >= 500:
        discount = subtotal * 0.10
    elif subtotal >= 250:
        discount = subtotal * 0.05
    else:
        discount = 0

    final_total = subtotal - discount

    print(f"Subtotal: Rs.{subtotal:.2f}")
    print(f"Discount: Rs.{discount:.2f}")
    print(f"Final total: Rs.{final_total:.2f}")
    print("Thank you!")
