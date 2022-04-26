'''
Condiçoes IF, ELIF, e ELSE - aula 4
== > >= < <= != (diferente)
'''

# num_1 = 2 #int
# num_2 = '2' #string
# expressao = (num_1 == num_2)
#
# print(expressao)

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

#Limite para a idade pegar emprestismo
muito_jovem = 20
muito_velho = 30

if idade >= muito_jovem and muito_velho:
    print(f'{nome} pode pegar emprestimo.')
else:
    print(f'{nome} nao pode pegar.')

