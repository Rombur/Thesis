pdf : main.tex\
	Cross_Sections/cross_sections.tex\
	Boltzmann_Equations/boltzmann_equations.tex\
	biblio.bib
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex

.PHONY : clean

clean : 
	-rm main.pdf
	-rm *.log *.aux *.bbl *.blg
