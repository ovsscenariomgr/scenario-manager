default: clean build run

build:
	docker compose build

run:
	docker compose up -d --wait

clean:
	docker compose down --volumes