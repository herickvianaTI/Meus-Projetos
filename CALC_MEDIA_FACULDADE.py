print(' ########################################################### ')
print(' #                                                         # ')
print(' # SEJA BEM VINDO(A) A CALCULADORA UNIVERSITÁRIA DE MÉDIAS # ')
print(' #                                                         # ')
print(' ########################################################### ')

print('                                                             ')

print('INSIRA A NOTA DA AV1: ')
AV1 = float(input())

print('                                                             ')

print('INSIRA A NOTA DA AV2: ')
AV2 = float(input())

print('                                                             ')

MEDIA = (AV1 + AV2) / 2

if MEDIA >= 7.0:  
    print('APROVADO')
else:
    print('INSIRA A NOTA DA AVS: ')
AVS = float(input())

if AVS >= 6.0:
    print('APROVADO')
else:
    print('REPROVADO POR MÉDIA')
AVS = float(input())