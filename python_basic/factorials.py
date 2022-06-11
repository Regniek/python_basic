def factorial(n):
  """
    Calculate the n factorial.

    n int > 0
    returns n!
  """
  print(n)
  if n == 1:
    return 1
  return n * factorial(n-1)

n = int(input('Write a integer: '))

print(factorial(n))