import os

def my_cook_book():
  with open('Recipes.txt', encoding='utf-8') as file:

    cook_book = {}

    for txt in file.read().split('\n\n'):
      name, _, *args = txt.split('\n')
      temporary_file = []
      for arg in args:
        ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
        temporary_file.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
      cook_book[name] = temporary_file

  return cook_book

cook_book = my_cook_book()
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):

  ingredient_list = dict()

  for dish in dishes:
    if dish in cook_book:
      for ingredients in cook_book[dish]:
        new_shop_list = dict()
        if ingredients['ingredient_name'] not in ingredient_list:
          new_shop_list['measure'] = ingredients['measure']
          new_shop_list['quantity'] = ingredients['quantity'] * person_count
          ingredient_list[ingredients['ingredient_name']] = new_shop_list
        else:
          ingredient_list[ingredients['ingredient_name']]['quantity'] = ingredient_list[ingredients['ingredient_name']]['quantity'] + ingredients['quantity'] * person_count
    else:
      print(f"Такого блюда нет в списке")
  return ingredient_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
