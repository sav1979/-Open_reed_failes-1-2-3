# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:39:12 2022

@author: sklad_2
"""
from pprint import pprint
import json

def get_cook_book(text_file):
    text_file = 'dishe.txt'
    with open(text_file, 'r') as my_file:
        cook_book = {}
        for dish in my_file:
            dish_name = dish.strip()
            count = int(my_file.readline())
            ingredients_list = []
            for i in range(count):
                ingredients = my_file.readline().strip()
                splited = ingredients.split('|')
                ingredients_dict = dict()
                ingredients_dict['ingredient_name'] = splited[0]
                ingredients_dict['quantity'] = int(splited[1])
                ingredients_dict['measure'] = splited[2]
                ingredients_list.append(ingredients_dict)
                my_file.readline()
                cook_book[dish_name] = ingredients_list

# print()
    return cook_book

loc_cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    ingeridients = {}
    for dish in dishes:
        if dish in loc_cook_book.keys():
            for ingredient in loc_cook_book[dish]:
                if ingredient['ingredient_name'] not in ingeridients:
                    ingeridients[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': (person_count*ingredient['quantity']) }
                else:
                    ingeridients[ingredient['ingredient_name']]['quantity'] += person_count*ingredient['quantity']
    return ingeridients

def main():
    result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    print(result)

main()