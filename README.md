# Introduction

Raton is from-scratch rebuild of my Yenot framework.  The goal is to tie
parameterized HTTP routes to Python functions with built-in connection to a
PostgreSQL database.  A library of SQL convenience functions for read and write
are included.  These support annotating results sets with PG types and writing
deserialized HTTP bodies to the database.

The goal is not to be an ORM but to provide the tools that allow and encourage
direct access to raw SQL.

# Tooling

Raton is built on a few carefully selected foundational libraries including
primarily [Starlette](https://pypi.org/project/starlette/) and
[Psycopg](https://pypi.org/project/psycopg/).

There is nothing fundamentally linked to Docker in the architecture of Raton
but containers have proven to be a convenient development tool and the
deployment documentation assumes a docker environment.  The included
docker-compose.yml may be a useful template to pattern for your own deployment
but it is recommended build your own.  For one certainty you will need to
provide some distinction in your environmental configuration for the database
access.
