#read product code and item quantity
product_code, item_quantity = input().split()

#convert string to int
product_code = int(product_code)
item_quantity = int(item_quantity)

#calculate the total value to be paid
total = 0.0
if product_code == 1:
	total = 4 * item_quantity
elif product_code == 2:
	total = 4.5 * item_quantity
elif product_code == 3:
	total = 5 * item_quantity
elif product_code == 4:
	total = 2 * item_quantity
elif product_code == 5:
	total = 1.5 * item_quantity

#print value to pay
print(f"Total: R$ {total:.2f}")
