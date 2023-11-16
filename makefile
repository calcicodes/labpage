.PHONY: papers html deploy

papers:
	python assets/scripts/papers/build_papers.py

deploy:
	git pull
	JEKYLL_ENV=production
	bundle exec jekyll build --destination /var/www/biomin

local:
	bundle exec jekyll serve