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


def record_file(path_1=None, path_2=None, path_3=None):
  if path_1 or path_2 or path_3 is None:
    path_1 = '1.txt'
    path_2 = '2.txt'
    path_3 = '3.txt'

    new_file = "rewrite_file.txt"

    file_1_path = os.path.join(os.getcwd(), path_1)
    file_2_path = os.path.join(os.getcwd(), path_2)
    file_3_path = os.path.join(os.getcwd(), path_3)

    with open(file_1_path, 'r', encoding='utf-8') as f1:
      file_1 = f1.readlines()
    with open(file_2_path, 'r', encoding='utf-8') as f2:
      file_2 = f2.readlines()
    with open(file_3_path, 'r', encoding='utf-8') as f3:
      file_3 = f3.readlines()

    with open(new_file, 'w', encoding='utf-8') as f_total:
      if len(file_1) < len(file_2) and len(file_1) < len(file_3):
        f_total.write(path_1 + '\n')
      elif len(file_2) < len(file_1) and len(file_2) < len(file_3):
        f_total.write(path_2 + '\n')
        f_total.write(str(len(file_2)) + '\n')
        f_total.writelines(file_2)
        f_total.write('\n')
      elif len(file_3) < len(file_1) and len(file_3) < len(file_2):
        f_total.write(path_3 + '\n')
        f_total.write(str(len(file_3)) + '\n')
        f_total.writelines(file_3)
        f_total.write('\n')
      if len(file_2) > len(file_1) > len(file_3) or len(file_2) < len(file_1) < len(file_3):
        f_total.write(path_1 + '\n')
        f_total.write(str(len(file_1)) + '\n')
        f_total.writelines(file_1)
        f_total.write('\n')
      elif len(file_1) > len(file_2) > len(file_3) or len(file_2) > len(file_1) and len(file_2) < len(file_3):
        f_total.write(path_2 + '\n')
        f_total.write(str(len(file_2)) + '\n')
        f_total.writelines(file_2)
        f_total.write('\n')
      elif len(file_1) > len(file_3) > len(file_2) or len(file_3) > len(file_1) and len(file_3) < len(file_2):
        f_total.write(path_3 + '\n')
        f_total.write(str(len(file_3)) + '\n')
        f_total.writelines(file_3)
        f_total.write('\n')
      if len(file_1) > len(file_2) and len(file_1) > len(file_3):
        f_total.write(path_1 + '\n')
        f_total.write(str(len(file_1)) + '\n')
        f_total.writelines(file_1)
      elif len(file_2) > len(file_1) and len(file_2) > len(file_3):
        f_total.write(path_2 + '\n')
        f_total.write(str(len(file_2)) + '\n')
        f_total.writelines(file_2)
      elif len(file_3) > len(file_1) and len(file_3) > len(file_2):
        f_total.write(path_3 + '\n')
        f_total.write(str(len(file_3)) + '\n')
        f_total.writelines(file_3)
  else:
    print("")
  return

record_file()