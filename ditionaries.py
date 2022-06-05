my_dict = {
  'david':35,
  'erika':32,
  'jaime':50,
}

print(my_dict['david'])

print(my_dict.get('juan',30))

my_dict['jaime']=20

print(my_dict)

my_dict['pedro']=70

print(my_dict)

del my_dict['jaime']

print(my_dict)

for llave in my_dict.keys():
  print(llave)

for valor in my_dict.values():
  print(valor)

for llave, valor in my_dict.items():
  print(llave, valor)

print('david' in my_dict)