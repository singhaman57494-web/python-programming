#                               mini shopping cart

cart = {
    "Laptop" : 55000,
    "Mouse" : 1200,
    "Keyboard" : 2500,
    "headphones" : 3000,
    "USB cable" : 500
}
total = 0
expensive = []
max_price = 0
key = ""

for name, price in cart.items():
    total += price
    if price >= 2000:
        expensive.append(name)
    if price > max_price:
        max_price = price
        key = name

print("TOTAL : ", total)

print("Expensive items : ", expensive)
print("Most expensive : ", key, max_price)
if total > 6000:
    print("CUSTOMER TYPE : Premium customer")
else:
    print("Regular Customer")
