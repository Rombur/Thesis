pdf : main.tex\
	Introduction/introduction.tex\
	Boltzmann_Equations/boltzmann_equations.tex\
	Boltzmann_Equations/fp_xs.tex\
	Boltzmann_Equations/galerkin.tex\
	Dsa/algebraic_multigrid.tex\
	biblio.bib
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main

.PHONY : clean

clean : 
	-rm main.pdf
	-rm *.log *.aux *.bbl *.blg
