GITHUB_PAGES_BRANCH=gh-pages
SITENAME=cvillemathcircle

html:
	hugo --theme=srg

develop:
	hugo server --theme=srg --watch

github: html
	git add -A
	git commit -m "Rebuilt site"
	git push origin master
	git subtree push --prefix=public https://evansuva@github.com/evansuva/$(SITENAME).git gh-pages


.PHONY: html clean develop
