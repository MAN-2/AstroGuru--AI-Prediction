from fastapi import FastAPI, Request , Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from ai import construct_prompt , get_ai_response

app= FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates= Jinja2Templates(directory="temp")

DEBUG_MODE = True # for one time question cookie ,

@app.get("/", response_class=HTMLResponse) #starting
async def read_index(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/form", response_class=HTMLResponse)
async def form(request:Request):
    return templates.TemplateResponse("form.html",{"request": request})


@app.post("/submit", response_class=HTMLResponse)
async def submit(request:Request,
                 name:str =Form(...),
                 date:str =Form(...),
                 time:str =Form(...),
                 place:str =Form(...),
                 question:str= Form(None)):
    
    used_free = request.cookies.get("used_free")
    if not DEBUG_MODE:
        used_free = request.cookies.get("used_free")
    if used_free == "true":
        #  free request, show premium 
        context = {
            "request": request,
            "premium": True
        }
        
        return templates.TemplateResponse("results.html", context)
        
    prompt=construct_prompt(name ,date , time , place ,question)
    ai_response= await get_ai_response(prompt)
    context={
        "request":request,
        "name":name,
        "date":date,
        "time": time,
        "place": place,
        "ai_response": ai_response,
        "premium":False
    }
    response = templates.TemplateResponse("results.html", context)
    response.set_cookie(key="used_free", value="true", max_age=60*60*24*30)  
    return response




if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

