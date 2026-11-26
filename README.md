# Watermelon ripeness thesis manuscript

The main document is `thesis.TEX` (uppercase extension). Select this file as the main document in Overleaf and use pdfLaTeX. For a local build with TeX Live, run the following commands in the project root.

```sh
pdflatex thesis.TEX
bibtex thesis
pdflatex thesis.TEX
pdflatex thesis.TEX
```

Run pdfLaTeX again if the table of contents or lists still show earlier page numbers.

Chapters 1–5 are in `chapter1.tex` through `chapter5.tex`. The bibliography uses `references.bib` and the repository's APA style. The appendix text, exhibits, and forms are in `appendix.tex`. Appendices F–J use the original form pages by default. Set `\editablerecordstrue` in `commands.tex` to typeset their editable versions. Graphics are in `figures/`.
