# Filtering in Python
array: list[int] = [n for n in range(10) if n < 5]
print(array)

products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]

new_products = [
    {**product, 'price': product['price'] * 1.05} 
    if product['price'] > 20 else {**product}
    for product in products
    if product['price'] > 10
]
print(new_products)