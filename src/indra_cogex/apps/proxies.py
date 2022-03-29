"""Proxies for the web application.

The point of this module is to make it possible to access global state
of the web application in all the various modules that have blueprints,
without creating circular imports.
"""

from flask import current_app, request
from werkzeug.local import LocalProxy

from indra_cogex.apps.constants import INDRA_COGEX_EXTENSION
from indra_cogex.client.neo4j_client import Neo4jClient

__all__ = [
    "client",
    "limit",
]

client: Neo4jClient = LocalProxy(lambda: current_app.extensions[INDRA_COGEX_EXTENSION])


limit: int = LocalProxy(lambda: request.args.get("limit", type=int, default=25))
