# List comprehension in Python
# List comprehension is a quick way to create lists from iterables
# print(list(range(10)))

products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]

new_products = [
    {**product, 'price': product['price'] * 1.05} 
    if product['price'] > 20 else {**product}
    for product in products
]
# print(new_products)
print(*new_products, sep='\n')