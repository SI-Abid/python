import itertools

for i in itertools.count(0):
  num1 = int(input('Enter the first number: '))
  num2 = int(input('Enter the second number: '))
  ch = input("Enter which operation you want to perform: ")
  result = 0
  # switch case
  switcher = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2,
  }
  result = switcher.get(ch, "Undefined")
  print(num1,ch,num2,":",result)
  d = input('Enter go/exit: ')
  if d=='exit':
    break
