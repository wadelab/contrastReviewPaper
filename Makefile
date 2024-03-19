all: 
	make document

document:	
	docker-compose run --rm document

document-docker: 
	R -e "xfun::pkg_attach2('rmarkdown')"
	R -e "rmarkdown::render('review.qmd',output_format='html_document')"