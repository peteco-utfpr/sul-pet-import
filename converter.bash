#!/usr/bin/env bash

if [ ! -d ./txt ]; then
  mkdir -p ./txt;
fi

for f in $(ls ./arquivo_ordenado)
	do
		if [[ $f == *.docx ]]
		then
			doc2pdf ./arquivo_ordenado/$f
		fi
	done

for f in $(ls ./arquivo_ordenado)
	do
		if [[ $f == *.pdf ]]
		then
			pdftotext ./arquivo_ordenado/$f
		fi
	done

mv ./arquivo_ordenado/*.txt ./txt