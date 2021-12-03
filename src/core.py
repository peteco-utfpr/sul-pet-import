from numpy.core.numeric import False_
import pandas as pd
import wget
import os

df = pd.read_csv('../input/dados.csv',sep=';')

aprovados = df[df['Situação']=='Aprovado']

ordenados = aprovados.sort_values(
	['Título do trabalho', 'Data da Submissão'], ascending=[True, False])

agrupados = ordenados.groupby(
	by='Título do trabalho').first().reset_index()

agrupados = agrupados.sort_values(
	['Número Único do Trabalho','Data da Submissão'], ascending=[True, False])

agrupados = agrupados.groupby(
	by='Número Único do Trabalho').first().reset_index()

if not os.path.exists('../arquivos'):
	os.mkdir('../arquivos')

# new_column_for_file = []

for (i,s) in agrupados.iterrows():
	print("\n------------\nTrabalho: {0}\nLink:".format(s['Título do trabalho']))
	file_format = str(s['Trabalho completo']).split('.')[-1]
	print(s['Trabalho completo'], '\nSalvando como (./arquivos/): {0}.{1}'.format(
		s['Título do trabalho'],file_format))
	
	try:
		if not os.path.exists('../arquivos/{0}.{1}'.format(
				s['Título do trabalho'],file_format)):
			wget.download(s['Trabalho completo'], '../arquivos/{0}.{1}'.format(
				s['Título do trabalho'],file_format))
		else:
				print('Arquivo já baixado.')
		
		# new_column_for_file.append('{0}.{1}'.format(
		# 	s['Título do trabalho'],file_format))

		print('\n\t-> OK!\n------------')

	except:
		print('ERRO:\n', s['Trabalho completo'], \
		'\n./arquivos/{0}.{1}'.format(s['Título do trabalho'],file_format))

if not os.path.exists('../out'):
		os.mkdir('../out')

l = []
for (i,s) in agrupados.iterrows():
	row = {}
	row['Título'] = str(s['Título do trabalho'])
	row['Autores'] = str(s['Nome do participante']) + \
		', ' + str(s['Coautores do trabalho'])
	
	l.append(row)

df = pd.DataFrame(l)

df.to_csv('../out/sumario.csv', index=False)
agrupados.to_csv('../out/metadados.csv', index=False)