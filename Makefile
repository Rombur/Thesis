pdf : main.tex\
	Cross_Sections/cross_sections.tex\
	biblio.bib
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex

.PHONY : clean

clean : 
	-rm main.df
	-rm *.log
