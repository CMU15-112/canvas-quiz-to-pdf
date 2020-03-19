TEX_FILES := $(wildcard *.tex)
PDF_FILES := $(addsuffix .pdf,$(basename $(TEX_FILES)))

all: $(PDF_FILES)

#Build the pdfs
%.pdf : %.tex
	pdflatex $<

clean:
	rm -f *.out
	rm -f *.log
	rm -f *.aux
	rm -f *.pdf
	rm -rf _minted*
