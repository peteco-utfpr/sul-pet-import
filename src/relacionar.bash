#!/usr/bin/env bash
# -*- coding: utf-8 -*-

echo ''
echo '************************'
echo '************************'
echo '************************'
echo '\t RELACIONAR.BASH'
echo '************************'
echo '************************'
echo '************************'

if [ -f ../out/relacao.csv ]
then
	rm ../out/relacao.csv
fi

for f in $(ls ../out/txt)
do
	title=$(head -n 6 "../out/txt/${f}")
	echo "'${title}';'${f}'" >> ../out/relacao.csv
done