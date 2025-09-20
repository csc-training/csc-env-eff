LECTURES= \
00_account_and_project.md \
01_logging_in.md 
# csc-env.md creates the index for allas

TITLE=Title.pdf

PRESS=csc-env-press.pdf
HANDOUT=csc-env--handout.pdf

#PANDOC=$(HOME)/bin/pandoc-eurocc.sif
PANDOC=pandoc-eurocc.sif   # Cases when pandoc is elsewhere and that folder is in PATH

HTMLS:=$(patsubst %.md,%.html,$(LECTURES))
PDFS:=$(patsubst %.md,%.pdf,$(LECTURES))

all: $(PDFS)
	echo -c $(TITLE) -o $(PRESS) -h $(HANDOUT) -- $(PDFS)

%.html:%.md
	$(PANDOC) -s $<

%.pdf:%.html
	echo $<

.PHONY: clean

# Note, set up allas-conf first!
intoAllas: $(HTMLS)

	a-put -n --override -b CSC_training $(HTMLS)

clean:
	-/bin/rm -f $(HTMLS) $(PDFS) $(PRESS) $(HANDOUT) *~

.PRECIOUS: %.html
