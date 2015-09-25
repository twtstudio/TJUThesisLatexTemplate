del *.aux /s
del *.bak /s
del *.log /s

del *.bbl /s
del *.dvi /s
del *.blg /s
del *.thm /s
del *.toc /s
del *.toe /s

del *.lof 
del *.lot
del *.out 

del *.fen
del *.ten
del *.ps

del *.loa

set ARTICLE=tjumain
latex -synctex=1 %ARTICLE%
bibtex %ARTICLE%
latex -synctex=1 %ARTICLE%
latex -synctex=1 %ARTICLE%
dvipdfmx  %ARTICLE%.dvi
start %ARTICLE%.pdf
