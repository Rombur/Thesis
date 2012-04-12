pdf : main.tex\
	Boltzmann_Equations/boltzmann_equations.tex\
	biblio.bib
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main

.PHONY : clean

clean : 
	-rm main.pdf
	-rm *.log *.aux *.bbl *.blg
