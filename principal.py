import uteis

uteis.menu()

try:
    escolha = int(input('Digite um número inteiro: '))

except:
    val = str(input(('Digite uma opção válida: ')))
    uteis.menu()

if escolha == 1:
    print('Bem-vindo de volta! Estamos prontos para te ajudar a alcançar seus objetivos.')

elif escolha == 2:
    name = str(input('Digite seu nome: '))
    idade = int(input('Sua idade: '))
    cpf = int(input('Digite seu CPF, pode usar pontos: '))
    print(f'Prazer {name}, sua idade é {idade} e seu CPF é {cpf}')


elif escolha == 3:
    print('Agradecemos seu contato até mais!')
    volta = str(input('Deseja voltar? [S/N]')).strip().upper()[0]
    if volta =='S':
        uteis.menu()
        try:
            escolha = int(input('Digite um número inteiro: '))
        except:
            uteis.menu()
            val = str(input(('Digite uma opção válida: ')))
        else:
            print('Certo te respeito, mas estamos aqui, qualquer coisa!')


else:
    uteis.menu()
    val = str(input(('Digite uma opção válida: ')))
