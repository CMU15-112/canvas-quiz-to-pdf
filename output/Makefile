TEX_FILES := $(wildcard *.tex)
PDF_FILES := $(addsuffix .pdf,$(basename $(TEX_FILES)))

all: $(PDF_FILES)

#Build the pdfs
%.pdf : %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<

