from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import pathlib

# Get the current directory
current_dir = pathlib.Path(__file__).parent.absolute()

# Create required directories relative to the current file
templates_dir = current_dir / "templates"
static_dir = current_dir / "static"
os.makedirs(templates_dir, exist_ok=True)
os.makedirs(static_dir / "css", exist_ok=True)
os.makedirs(static_dir / "js", exist_ok=True)
os.makedirs(static_dir / "images", exist_ok=True)

app = FastAPI()

# Mount static files directory with absolute path
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Set up templates with absolute path
templates = Jinja2Templates(directory=str(templates_dir))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    print(f"Templates directory: {templates_dir} exists: {os.path.exists(templates_dir)}")
    print(f"Looking for: {templates_dir / 'index.html'} exists: {os.path.exists(templates_dir / 'index.html')}")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})  # Change to contact.html when created

@app.get("/resume", response_class=HTMLResponse)
async def resume(request: Request):
    # You can create a specific resume page or redirect to a PDF
    return templates.TemplateResponse("resume.html", {"request": request})
    # Alternatively, to serve a PDF:
    # return FileResponse("static/files/resume.pdf")

@app.get("/favicon.ico", response_class=FileResponse)
async def favicon():
    return FileResponse("static/favicon.ico")

# Simple debugging endpoint to check template existence
@app.get("/debug")
async def debug():
    templates_dir = current_dir / "templates"
    index_path = templates_dir / "index.html"
    
    return {
        "current_dir": str(current_dir),
        "templates_dir": str(templates_dir),
        "templates_dir_exists": os.path.exists(templates_dir),
        "index_path": str(index_path),
        "index_exists": os.path.exists(index_path),
        "templates_contents": os.listdir(templates_dir) if os.path.exists(templates_dir) else "Directory doesn't exist"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 