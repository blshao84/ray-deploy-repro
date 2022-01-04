from fastapi import FastAPI
from ray import serve
from starlette.requests import Request
from starlette.responses import Response

from deploytest.foo.bar.foobar import foobar

serve_app = FastAPI()


@serve.deployment(num_replicas=1)
@serve.ingress(app=serve_app)
class Api(object):
    @serve_app.post("/foobar", response_class=Response)
    async def payoff(self, req: Request):
        data = await req.body()
        print(data)
        res = foobar()
        return Response(content=res)
