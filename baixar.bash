#!/usr/bin/env bash

# Cria pasta se não existir
if [ ! -d ./arquivo_bruto ]; then
  mkdir -p ./arquivo_bruto;
fi

cd ./arquivo_bruto

# Baixa os arquivos na pasta criada
for f in $(cat "../lista_sulpet.csv")
	do
	echo "baixando: $f"
	wget $f
done

cd -
