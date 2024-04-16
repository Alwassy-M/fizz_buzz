def fizz_buzz(value):
  for num in range(value):
    if num % 3 == 0:
      print('fizz')
    elif num % 5 == 0:
      print('buzz')
    elif num % 3 == 0 and num % 5 == 0:
      print('fizzbuzz')
    else:
      print(num)
   

fizz_buzz(100)
