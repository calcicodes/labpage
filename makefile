.PHONY: papers html deploy

papers:
	python assets/scripts/papers/build_papers.py

deploy:
	git pull
	bundle exec jekyll build --destination /var/www/biomin
