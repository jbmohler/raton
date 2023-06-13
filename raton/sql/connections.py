import urllib.parse
import psycopg
from psycopg_pool import ConnectionPool


async def create_connection(dburl):
    result = urllib.parse.urlsplit(dburl)

    kwargs = {"dbname": result.path[1:]}
    if result.hostname != None:
        kwargs["host"] = result.hostname
    if result.port != None:
        kwargs["port"] = result.port
    if result.username != None:
        kwargs["user"] = result.username
    if result.password != None:
        kwargs["password"] = result.password

    return await psycopg.connect(**kwargs)


async def create_pool(dburl):
    result = urllib.parse.urlsplit(dburl)

    kwargs = {"dbname": result.path[1:]}
    if result.hostname not in [None, ""]:
        kwargs["host"] = result.hostname
    if result.port != None:
        kwargs["port"] = result.port
    if result.username != None:
        kwargs["user"] = result.username
    if result.password != None:
        kwargs["password"] = result.password
    # kwargs["cursor_factory"] = psycopg2.extras.NamedTupleCursor

    return ConnectionPool(min_size=3, max_size=6, kwargs=kwargs)
