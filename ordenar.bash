#!/usr/bin/env bash

if [ ! -d ./arquivo_ordenado ]
then
  mkdir ./arquivo_ordenado
fi

if [ -f ./map_ordenacao ]
then
  rm ./map_ordenacao.csv
fi

n=1

for f in $(ls ./arquivo_bruto)
	do
		filen=$(printf "%.6d" "${n}")
		if [[ $f == *.pdf ]] || [[ $f == *.pdf.* ]]
		then
			cp ./arquivo_bruto/$f ./arquivo_ordenado/$filen.pdf
			echo "'$f';'$filen'" >> map_ordenacao.csv
			let n++
		else 
			if [[ $f == *.docx ]] || [[ $f == *.docx.* ]]
			then
				cp ./arquivo_bruto/$f ./arquivo_ordenado/$filen.docx
				echo "'$f';'$filen'" >> map_ordenacao.csv
				let n++
			fi
		fi		
	done
