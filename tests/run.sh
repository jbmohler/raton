set -e

./dev/server.sh up_server

until $(curl --output /dev/null --silent --fail http://localhost/api/ping); do
	printf	'-'
	sleep .5
done

printf '>\n'

curl --fail http://localhost/api/info

# carriage return to skip to next line and not be overwritten by
# docker compose down
printf '\n*** TESTS COMPLETE ***\n'

docker compose logs raton-api

./dev/server.sh down_server
