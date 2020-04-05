def abs(n):
  if n < 0:
    return n * -1
  return n

def square(x):
  return x * x

def is_good_enough(guess, n):
  return abs((square(guess) - n)) < 0.0000000001

# abs(guess * guess - n) > 0.0000000001

def average(a, b):
  return (a + b) / 2

def improve_guess(guess, n):
  return average (guess, n / guess)

def sqrt(n):
  guess = 1

  while not is_good_enough(guess, n):
    guess = improve_guess(guess, n)
  return guess

print(sqrt(2))
print(sqrt(25))
