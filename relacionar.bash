#!/usr/bin/env bash

if [ -f relacao.csv ]
then
	rm relacao.csv
fi

for f in $(ls ./txt)
do
	title=$(head -n 5 ./txt/$f)
	echo "'${title}';'${f}'" >> relacao.csv
done