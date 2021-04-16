"""
https://fastapi.tiangolo.com/advanced/custom-response/#html-response
"""

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates/")





@app.get("/")
def form_post(request: Request):
    return templates.TemplateResponse(
        "form.html", context={"request": request}
    )


@app.post("/")
async def form_post(request: Request):
    form_data = await request.form()
    return "ok"