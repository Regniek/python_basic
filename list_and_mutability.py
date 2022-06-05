#list methods append pop remove insert
my_list=[1,2,3]

print(my_list[1:])

my_list.append(4)

print(my_list)

my_list[0]='Hola'

print(my_list)

my_list.pop()

print(my_list)


for element in my_list:
  print(element)

a = [1,2,3]

b = a

c = [a,b]

print(id(a))
print(id(b))
print(id(c))
print(a)
print(b)
print(c)

a.append(5)
print(a)
print(b)
print(c)

#clon list or generate with new list

a = [1,2,3]
print(a)
print(id(a))

b = a

print(id(b))
print(b)
c = list(a)

print(id(c))
print(c)

d = a[::]

print(id(d))
print(d)

#list comprehension similar to map in other legunajes

my_list = list(range(100))

print(my_list)

double = [i * 2 for i in my_list]

print(double)

pares = [i for i in my_list if i % 2 == 0]

print(pares)