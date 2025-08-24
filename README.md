# Astrology AI Web App with GSAP Animations
An interactive astrology web application built with FastAPI backend and React frontend with GSAP animations. The app uses Large Language Model (LLM) API calls to generate personalized astrological predictions, sun sign insights, strengths, challenges, short forecasts, and practical remedies or advice for personal betterment.

# Features
* Personalized astrology predictions about a user persona generated using LLM API calls.

* Displays sun sign, individual strengths, challenges, and a short astrological forecast.

* Provides actionable remedies and insights for self-improvement.

* Interactive, smooth animations implemented via GSAP on the frontend.

* Backend serves dynamic HTML templates using Jinja2 and serves static assets like JS, CSS, and images.

* Clean and modern UI with responsive design.

# Demo and Screemshots


https://github.com/user-attachments/assets/c6050ab5-0b9f-40d4-bd3f-25e5a7473461

![Screenshot 2025-08-24 111649](https://github.com/user-attachments/assets/cddf0adb-cd6f-42f1-abd2-da32a1dbdb9b)





# Tech Stack
* Backend: FastAPI (Python), Jinja2 templates

* Frontend: React, GSAP (GreenSock Animation Platform)

* LLM Integration: External LLM providers via API calls

* Static files served via FastAPI’s StaticFiles from a /static directory

# Installation
Clone the repository

bash
git clone https://github.com/MAN-2/AstroGuru--AI-Prediction.git

Backend Setup

bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Frontend Setup

bash
cd frontend
npm install
npm start

# Environment Configuration

* Add your LLM API keys and endpoint URLs in .env files or environment variables as needed.

* Verify static files are placed in the static folder at the backend root.

* Jinja2 templates should be in the temp directory.

* FastAPI Configuration
Static files like CSS, JS, and images are served from /static URL path:

python
app.mount("/static", StaticFiles(directory="static"), name="static")
Jinja2 templates for HTML renderings are stored in the temp folder:

python
templates = Jinja2Templates(directory="temp")
Templates can link static files by referring to /static/filename.

# Usage
* Enter birth details or persona info into the frontend form.

* Click “Generate Prediction” to call the backend API.

* Backend sends a prompt to the LLM API, which returns personalized predictions.

* The frontend receives results and showcases predictions.

* Explore strengths, challenges, forecasts, and remedies with obtained results.

* By default , the app is set to debug mode and will not ask for premium subscription after one question

* However, one can revert the variable state of DEBUG_MODE in main.py to switch back.

