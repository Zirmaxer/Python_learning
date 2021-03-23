stock = {
   'banana': 6,
   'apple': 0,
   'orange': 32,
   'pear': 15
  }
prices = {
   'banana': 4,
   'apple': 2,
   'orange': 1.5,
   'pear': 3
  }
# write your program here
price = 0
for key1, value1 in stock.items():
    for key2, value2 in prices.items():
        if key1 == key2:
            price += value1*value2
print (price)