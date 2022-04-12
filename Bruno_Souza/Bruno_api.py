# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13rjPsQPLCoyl8o8Gf0Fmpf24PQhnoiST
"""

import requests

def get_pokemon_names_from_ids(*ids):

  result = []

  for _id in ids:
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(_id)
    response = requests.get(url)
    r = response.json()

    abilities = [s['ability']['name'] for s in r['abilities']]
   

    name = r['name']
    weight = response.json()['weight']
    id =r['id']
    order = r['order']

    result.append(('Esse é o nome', name ,'essa é a habilidade', abilities ,' essa é o ID',  id ,' essa é o Pedido', order ))

  return result

get_pokemon_names_from_ids(1, 2, 3, 4)