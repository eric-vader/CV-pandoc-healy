default:
	pandoc -t html5 minimax.md -o minimax.pdf -s --pdf-engine=wkhtmltopdf
	pdfcrop minimax.pdf minimax.pdf
	pandoc -t html5 alphabeta.md -o alphabeta.pdf -s --pdf-engine=wkhtmltopdf
	pdfcrop alphabeta.pdf alphabeta.pdf