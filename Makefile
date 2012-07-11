pdf : main.tex\
	Introduction/introduction.tex\
	Boltzmann_Equations/boltzmann_equations.tex\
	Boltzmann_Equations/fp_xs.tex\
	Boltzmann_Equations/galerkin.tex\
	Anmg/introduction.tex\
	Anmg/anmg.tex\
	Anmg/results.tex\
	Anmg/conclusions.tex\
	Dsa/mip.tex\
	Dsa/algebraic_multigrid.tex\
	Dsa/results.tex\
	biblio.bib
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main

.PHONY : clean

clean : 
	-rm main.pdf
	-rm *.log *.aux *.bbl *.blg
