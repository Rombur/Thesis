pdf : 
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main

.PHONY : clean

clean : 
	-rm main.pdf
	-rm *.log *.aux *.bbl *.blg
