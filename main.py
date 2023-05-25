import fastapi

from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.cors import CORSMiddleware

import json
import time
import pytz

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")    

app = fastapi.FastAPI()


@app.get('/', response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("my_journey.html", {"request": request})

