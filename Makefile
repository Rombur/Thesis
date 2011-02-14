pdf : main.tex\
	Cross_Sections/cross_sections.tex
	pdflatex main.tex

.PHONY : clean

clean : 
	-rm main.df
	-rm *.log
