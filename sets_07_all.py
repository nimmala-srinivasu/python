fruits = {"apple", "orange", "banana", "apple", "pear", "papaya", "papaya"}
fruit_basket = {"apple", "banana", "grapes", "mango", "kiwi"}
print(fruits)
print(fruits & fruit_basket)    # print common
print(fruits | fruit_basket)    # print all no duplicate
print(fruits - fruit_basket)    # print not common from 1st set
print(fruits ^ fruit_basket)    # print not common all
print(len(fruit_basket))
print("pear" in fruits)
print("pear" not in fruit_basket)
print(fruits.issubset(fruit_basket))
print(fruits.issuperset(fruit_basket))
print(fruit_basket.copy())
