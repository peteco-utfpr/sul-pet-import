#!/usr/bin/env bash
# -*- coding: utf-8 -*-

echo ''
echo '************************'
echo '************************'
echo '************************'
echo '\tCONVERTER.BASH'
echo '************************'
echo '************************'
echo '************************'

if [ ! -d ../out/txt ]; then
  mkdir -p ../out/txt;
fi

for f in $(ls ../arquivos)
	do
		if [[ $f == *.docx ]]
		then
			echo "doc2pdf '../arquivos/${f}'" >> convert2doc.bash
			# doc2pdf "../arquivos/${f}"
		fi
	done

for f in $(ls ../arquivos)
	do
		if [[ $f == *.pdf ]]
		then
			echo "pdftotext '../arquivos/${f}'" >> convert2txt.bash
			# pdftotext "../arquivos/${f}"
		fi
	done

mv ../arquivos/*.txt ../out/txt