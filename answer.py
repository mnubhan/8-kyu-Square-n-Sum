def square_sum(numbers):
  totals=0
  for x in numbers:
     totals+=pow(x,2)
    
  return totals

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

def square_sum(numbers):
    return sum(x * x for x in numbers) 
