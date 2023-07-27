def sum_multiples(n):
  sum_of_multiples_of_3 = 0
  for i in range(1, n):
    if i - 3 == 0:
      sum_of_multiples_of_3 += i

  sum_of_multiples_of_5 = 0
  for i in range(1, n):
    if i - 5 == 0:
      sum_of_multiples_of_5 += i

  return sum_of_multiples_of_3 + sum_of_multiples_of_5

print(sum_multiples(100))

# not sure !!!