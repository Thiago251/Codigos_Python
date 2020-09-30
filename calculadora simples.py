mensagem = "por favor insira a operação matematica"
mensagem += "\n+ para adição"
mensagem += "\n- para subtração"
mensagem += "\n/ para divisão"
mensagem += "\n* para multiplicação \n+"

operação = input(mensagem)

num1 = int(input('Digite o numero: '))
num2 = int(input('Digite outro numero: '))

if operação == '+':
  print(f'Operação: {num1} {operação} {num2} = {num1 + num2}')
elif operação == '-':
  print(f'Operação: {num1} {operação} {num2} = {num1 - num2}')
elif operação =='/':
  print(f'Operação: {num1} {operação} {num2} = {num1 / num2}')
elif operação == '*':
  print(f'Operação: {num1} {operação} {num2} = {num1 * num2}')
else:
  print('operação matematica perfeita, o resultado e: {}'.format(operação))