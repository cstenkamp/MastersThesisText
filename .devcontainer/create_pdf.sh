python /workspace/tex_tools/acronyms2glossaries.py --filename /workspace/acronyms.txt -w
python /workspace/tex_tools/bib_add_howpublished.py /workspace/mendeley_bibs/Masterarbeit.bib
for s in $(ls /opt/input_data/); do docker exec -it mastersthesistext_devcontainer_pandoc_1 pandoc -t latex /opt/input_data/$s -o /opt/output_data/$(echo $s | sed 's/.md/.tex/g'); done
latexmk -r /workspace/.latexmkrc -synctex=1 -interaction=nonstopmode -file-line-error -pdf -outdir=/workspace /workspace/thesis.tex