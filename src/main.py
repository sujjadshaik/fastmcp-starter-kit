from fastapi import FastAPI, Request
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from mcp.server.sse import SseServerTransport
from server import mcp

app = FastAPI(title="FastAPI + MCP SSE")

sse = SseServerTransport("/messages/")


async def handle_sse(request: Request):
    async with sse.connect_sse(request.scope, request.receive, request._send) as (
        read,
        write,
    ):
        await mcp._mcp_server.run(
            read, write, mcp._mcp_server.create_initialization_options()
        )


mcp_app = Starlette(
    routes=[
        Route("/sse", endpoint=handle_sse, methods=["GET"]),
        Mount("/messages", app=sse.handle_post_message),
    ]
)

app.mount("/", mcp_app)
