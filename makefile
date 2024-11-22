.PHONY: papers html deploy

papers:
	python assets/scripts/papers/build_papers.py

deploy:
	git pull
	JEKYLL_ENV=production /home/ob266/.rvm/rubies/ruby-3.3.0/bin/bundle exec jekyll build --destination /var/www/biomin

local:
	JEKYLL_ENV=production bundle exec jekyll serve