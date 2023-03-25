
# Jogo de pedra, papel ou tesoura

import random

ppt=['pedra','papel','tesoura']

pt_maquina=0
pt_voce=0
empates=0

print('Jogo de pedra, papel ou tesoura:')

while True:

	maquina=random.choice(ppt)

	voce=input('Escolha pedra, papel ou tesoura: ')

	if voce=='pedra' and maquina=='pedra':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('Empatou!\n')
		empates=empates+1
	elif voce=='pedra' and maquina=='papel':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('A máquina venceu!\n')
		pt_maquina=pt_maquina+1
	elif voce=='pedra' and maquina=='tesoura':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('Você venceu!\n')
		pt_voce=pt_voce+1
	elif voce=='papel' and maquina=='pedra':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('Você venceu!\n')
		pt_voce=pt_voce+1
	elif voce=='papel' and maquina=='papel':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('Empatou!\n')
		empates=empates+1
	elif voce=='papel' and maquina=='tesoura':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('A máquina venceu!\n')
		pt_maquina=pt_maquina+1
	elif voce=='tesoura' and maquina=='pedra':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('A máquina venceu!\n')
		pt_maquina=pt_maquina+1
	elif voce=='tesoura' and maquina=='papel':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('Você venceu!\n')
		pt_voce=pt_voce+1
	elif voce=='tesoura' and maquina=='tesoura':
		print(f'Você escolheu {voce} e a máquina escolheu {maquina}!')
		print('Empatou!\n')
		empates=empates+1
	elif voce=='sair':
		print('Pontuação final:')
		print(f'Pontuação sua: {pt_voce}')
		print(f'Pontuação da máquina: {pt_maquina}')
		print(f'Empates {empates}')
		break
	else:
		print('Você digitou um valor invalido!\n')

