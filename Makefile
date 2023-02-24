image:
	docker build -t mycoins:1.0.0 .

run:
	docker run -p 5000:5000 --rm -d mycoins:1.0.0

tag:
	docker tag mycoins:1.0.0 kramerscs/mycoins:1.0.0

publish:
	docker push kramerscs/mycoins:1.0.0
