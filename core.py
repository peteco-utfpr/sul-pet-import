import pandas as pd
import wget
import os
import unidecode
import subprocess

def format_file_name(s:str):
	file_name = \
		str(s). \
		replace('/', '-'). \
		replace(':', '-'). \
		replace("\"",''). \
		replace("'",''). \
		replace(' ', '-'). \
		replace(',','-'). \
		replace('\\','-'). \
		replace('.',''). \
		strip(chr(34))[:25]

	file_name = unidecode.unidecode(file_name)

	count = 0
	while '"' in file_name:
		count += 1

		if count > 1:
			print('ERRO NA CONVERSAO DE NOME')
			exit(1)

		auxstr = ''
		for c in file_name:
			if c != '"':
				auxstr += c

		file_name = auxstr

	return file_name

df = pd.read_csv('./input/dados.csv',sep=';')

aprovados = df[df['Situação']=='Aprovado']

ordenados = aprovados.sort_values(
	['Título do trabalho', 'Data da Submissão'], ascending=[True, False])

agrupados = ordenados.groupby(
	by='Título do trabalho').first().reset_index()

agrupados = agrupados.sort_values(
	['Número Único do Trabalho','Data da Submissão'], ascending=[True, False])

agrupados = agrupados.groupby(
	by='Número Único do Trabalho').first().reset_index()

agrupados = agrupados.sort_values(
	['Título do trabalho', 'Data da Submissão'], ascending=[True, False])

if not os.path.exists('./arquivos'):
	os.mkdir('./arquivos')

for (i,s) in agrupados.iterrows():
	print("\n------------\nTrabalho: {0}\nLink:".format(s['Título do trabalho']))
	file_format = str(s['Trabalho completo']).split('.')[-1]

	file_name = format_file_name(str(s['Título do trabalho']))
	
	print(
	s['Trabalho completo'], '\nSalvando como (./arquivos/): {0}.{1}'.format(
	file_name, file_format))

	try:
		if not os.path.exists('./arquivos/{0}.{1}'.format(file_name,file_format)):
			wget.download(s['Trabalho completo'], './arquivos/{0}.{1}'.format(
				file_name, file_format))
		else:
				print('Arquivo já baixado.')
		
		print('\n\t-> OK!\n------------')
	
	except:
		print('ERRO:\n', s['Trabalho completo'], \
		'\n./arquivos/{0}.{1}'.format(s['Título do trabalho'],file_format))

if not os.path.exists('./out'):
		os.mkdir('./out')

agrupados.to_csv('./out/metadados.csv', index=False)

## Latex part 
tex_text = []

for (i,s) in agrupados.iterrows():
	title = '{' + s['Título do trabalho'] + '}'
	
	texto = str('\\addcontentsline{toc}{section}' + \
		'{0}\n'.format(title))

	file_name = format_file_name(str(s['Título do trabalho']))

	tex_text.append([texto,
		str('\includepdf' + \
			'{' + 'pdfs/{0}\n\n'.format(file_name)
		)
	])
			
with open('./out/trabalhos.tex','w+') as inc:
	for i in tex_text:
		inc.write(i[0])
		inc.write(i[1])

subprocess.run(['bash', 'convert.bash'])