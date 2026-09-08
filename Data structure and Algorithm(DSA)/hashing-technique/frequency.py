#             frequency count problem

today_orders = [
    "biryani", "Dosa", "biryani", "burger", 
    "Dosa", "biryani", "burger", "Dosa",
    "biryani"
]

def count_orders(orders):
    freq = {}

    for dish in orders:
        if dish in freq:
            freq[dish] = freq[dish] + 1
        else:
            freq[dish] = 1

    return freq

result = count_orders(today_orders)
print(result)