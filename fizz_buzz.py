def fizz_buzz(value):
  for num in range(1, value + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('fizzBuzz')
    elif num % 3 == 0:
      print('fizz')
    elif num % 5 == 0:
      print('buzz')
    else:
      print(num)

fizz_buzz(100)
