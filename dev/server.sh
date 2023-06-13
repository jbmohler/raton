
up_server() {
	docker compose up -d
}

init_server() {
	up_server
	# TODO prepare database
}

down_server() {
	docker compose down
}

get_wheels() {
	# This assumes a working Python on linux outside a docker
	rm -rf req-wheels
	mkdir req-wheels
	docker run --rm -u `id -u`:`id -g` -v ./:/build -w /build -v ./requirements.txt:/build/requirements.txt python:3.11 pip download -d /build/req-wheels -r /build/requirements.txt
	ls -la req-wheels
}

psql() {
        docker compose exec web python systools/admin-psql.py
}

"$@"
