import json
from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route


async def get_api_ping(request):
    return PlainTextResponse(".")


async def get_api_info(request):
    return JSONResponse({"server": "up"})


async def homepage(request):
    return JSONResponse({"hello": "world"})


context = {}


async def init_context():
    context["init"] = True

    from . import sql

    secrets = {}

    with open("/run/secrets/raton-config.json", "r") as ff:
        secrets = json.loads(ff.read())

    context["pool"] = await sql.create_pool(secrets["db.connection"])


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/api/ping", get_api_ping),
        Route("/api/info", get_api_info),
    ],
    on_startup=[init_context],
)
