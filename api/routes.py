from starlette.routing import Mount, Route
from starlette.responses import PlainTextResponse
from MyListAnalyzerAPI.routes import my_list_analyzer


async def greet(_):
    return PlainTextResponse(
        content="Hello There 2"
    )


main_route = Route("/", greet)

app_router = Mount(
    "/", routes=[
        my_list_analyzer, main_route
    ]
)
