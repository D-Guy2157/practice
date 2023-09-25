# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

# USD:
store = [("Shirt", 20.00),
         ("Pants", 25.00),
         ("jacket", 50.00),
         ("Socks", 10.00)]

to_cad = lambda data: (data[0], data[1]*1.28)
to_dollars = lambda data: (data[0], data[1]/1.28)

store_cad = list(map(to_cad, store))  # converts store(USD) to cad
store_dollars = list(map(to_dollars, store_cad))  # converts store cad back to USD
print("Original Store Prices(USD):")
for i in store:
    print(i)
print()
print("Prices in CAD:")
for i in store_cad:
    print(i)
print()
print("Prices in USD:")
for i in store_dollars:
    print(i)
