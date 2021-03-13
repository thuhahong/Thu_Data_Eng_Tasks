# lists
shopping_list = ["grapes", "blueberries", "mangoes", "strawberries", "apples"]

shopping_list[0] = "milk"
shopping_list.append("sugar")

print(shopping_list)
print(type(shopping_list))
print(len(shopping_list))
print(shopping_list[-3])
print(shopping_list[:5])
print(shopping_list[::2]) # start, finish, step size

# tuples are like lists however you cannot change the values inside
# tuples are immutable

#dictionaries

new_dict = {"my_key": "values",
            "num": 3,
            "key_list": ["val1", "val2", "val3"]}

print(new_dict)
print(new_dict['num'])
print(new_dict['key_list'][0])
print(new_dict.keys())

new_dict["my_key"] = "old_key" #to rename it
print(new_dict)