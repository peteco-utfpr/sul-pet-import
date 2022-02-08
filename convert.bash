cd ../arquivos

doc2pdf *.docx

rm *.docx

for file in *; do mv "${file}" "${file/\"/}"; done

cd -