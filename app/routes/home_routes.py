from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from starlette.config import Config

config = Config(".env")

templates = Jinja2Templates(directory="app/view_templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):

    serverTime: datetime = datetime.now().strftime("%d/%m/%y %H:%M:%S")
   
    return templates.TemplateResponse("index.html", {"request": request, "serverTime": serverTime })

@router.get("/advice", response_class=HTMLResponse)
async def advice(request: Request):
    requests_client = request.app.requests_client
    response = await requests_client.get(config("ADVICE_URL"))

    return templates.TemplateResponse("advice.html", {"request": request, "data": response.json() })


@router.get("/apod", response_class=HTMLResponse)
async def apod(request: Request):
    requests_client = request.app.requests_client
    response = await requests_client.get(config("NASA_APOD_URL") + config("NASA_API_KEY"))

    return templates.TemplateResponse("apod.html", {"request": request, "data": response.json() })


@router.get("/params", response_class=HTMLResponse)
async def params(request: Request, name : str | None = ""):

    return templates.TemplateResponse("params.html", {"request": request, "name": name })


@router.post("/clicked", response_class=HTMLResponse)
async def clicked(request: Request):
    return templates.TemplateResponse("./partials/clicked_button.html", {"request":request})


@router.get("/server_time", response_class=HTMLResponse)
async def index(request: Request):
    serverTime: datetime = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    return serverTime

