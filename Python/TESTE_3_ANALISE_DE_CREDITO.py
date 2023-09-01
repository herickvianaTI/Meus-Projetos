print ('#################################################################')
print ('#                                                               #')
print ('#     BEM VINDO AO SISTEMA DE ANÁLISE DE CRÉDITOS               #')
print ('#                                                               #')
print ('#################################################################')

print ('                                                                 ')

print (' INSIRA O VALOR DO EMPRÉSTIMO : ')
EMPRESTIMO = float(input())

print ('INSIRA O SEU SALÁRIO BRUTO MENSAL : ')
SALARIO = float(input())

if SALARIO >= 3000 and EMPRESTIMO <= 10000 :
    print('Parabéns, sua análise de empréstimo foi aprovada com sucesso!')


elif SALARIO >= 5000 and EMPRESTIMO <=20000 : 
      print('Parabéns, sua análise de empréstimo foi aprovada com sucesso!')


elif SALARIO >= 7000 and EMPRESTIMO <= 30000 :
      print('Parabéns, sua análise de empréstimo foi aprovada com sucesso!')


else :
     print('Sua análise de crédito não foi aprovada, escolha um valor menor') 