python /workspace/tex_tools/acronyms2glossaries.py --filename /workspace/acronyms.txt -w
python /workspace/tex_tools/bib_add_howpublished.py /workspace/mendeley_bibs/Masterarbeit.bib
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf -outdir=/workspace /workspace/thesis.tex