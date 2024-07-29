
empty_dict = {}
empty_dict2 = dict()
print(type(empty_dict))
print(type(empty_dict2))



filled_dict = {"name": "John", "age": 25, "profession": "Developer"}

print(filled_dict['Step'])
print(filled_dict.get("step", "Keyword Doesn't exist"))

filled_dict['courses'] = ['Python', 'Java', 'JavaScript', 'Go']
print(filled_dict)
print(filled_dict.keys())
print(filled_dict.values())
print(filled_dict.items())

for key, value in filled_dict.items():
    if key == 'name' and value == 'Irakli':
        print("Found")

    print(key, value)



filled_dict1 = {"name": "John", "age": 25, "profession": "Developer"}
filled_dict2 = {"last_name": "Doe", "courses": ['Python', 'Java']}

filled_dict.setdefault("last_name", 'Joe')
print(filled_dict)
filled_dict1.update(filled_dict2)
print(filled_dict1)


print(filled_dict1.pop('name'))
print(filled_dict1.popitem())

print('John' in filled_dict1)


frozen_dict = {frozenset({"John", "Kate"}): "Hello"}

print(frozen_dict[frozenset({"John", "Kate"})])


products = {'apple': 20, 'banana': 25, 'pinnaple': 21, 'orange': 22}

filtered_dict = {key: value for key, value in products.items() if value > 21}
print(filtered_dict)


products = {
    'electronics': {
        'laptops': {
            'apple': {
                1001: {'model': 'Macbook Pro', 'price': 6000},
                1002: {'model': 'Macbook Air', 'price': 4000}
            },
            'HP': {
                2001: {'model': 'Pavillion', 'price': 2000},
                2002: {'model': 'G250', 'price': 2000}
            }
        },
        'phones': {
            'samsung': {
                3001: {'model': "S24 Ultra", 'price': 2000}
            }
        }
    },
    'clothes': {
        'shirts': {
            'Nike': {
                4001: {'ragac key': 'ragac value'}
            }
        }
    }
}

print(products['electronics']['laptops']['apple'][1001]['price'])