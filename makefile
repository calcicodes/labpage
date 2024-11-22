.PHONY: papers html deploy

papers:
	python assets/scripts/papers/build_papers.py

deploy:
	git pull
	source ~/.rvm/scripts/rvm && rvm use 3.3.0
	JEKYLL_ENV=production bundle exec jekyll build --destination /var/www/biomin

local:
	JEKYLL_ENV=production bundle exec jekyll serve