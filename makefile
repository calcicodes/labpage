.PHONY: papers html

papers:
	python assets/scripts/papers/build_papers.py

html:
	bundle exec jekyll build
