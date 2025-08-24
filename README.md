# Astrology AI Web App with GSAP Animations
An interactive astrology web application built with FastAPI backend and React frontend with GSAP animations. The app uses Large Language Model (LLM) API calls to generate personalized astrological predictions, sun sign insights, strengths, challenges, short forecasts, and practical remedies or advice for personal betterment.

# Features
* Personalized astrology predictions about a user persona generated using LLM API calls.

Displays sun sign, individual strengths, challenges, and a short astrological forecast.

Provides actionable remedies and insights for self-improvement.

Interactive, smooth animations implemented via GSAP on the frontend.

Backend serves dynamic HTML templates using Jinja2 and serves static assets like JS, CSS, and images.

Clean and modern UI with responsive design.

Tech Stack
Backend: FastAPI (Python), Jinja2 templates

Frontend: React, GSAP (GreenSock Animation Platform)

LLM Integration: External LLM providers (e.g., OpenRouter, Gemini) via API calls

Static files served via FastAPI’s StaticFiles from a /static directory

Installation
Clone the repository

bash
git clone https://github.com/your-username/astrology-ai-gsap.git
cd astrology-ai-gsap
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
Environment Configuration

Add your LLM API keys and endpoint URLs in .env files or environment variables as needed.

Verify static files are placed in the static folder at the backend root.

Jinja2 templates should be in the temp directory.

FastAPI Configuration
Static files like CSS, JS, and images are served from /static URL path:

python
app.mount("/static", StaticFiles(directory="static"), name="static")
Jinja2 templates for HTML renderings are stored in the temp folder:

python
templates = Jinja2Templates(directory="temp")
Templates can link static files by referring to /static/filename.

Usage
Enter birth details or persona info into the frontend form.

Click “Generate Prediction” to call the backend API.

Backend sends a prompt to the LLM API, which returns personalized predictions.

The frontend receives results and animates their display using GSAP.

Explore strengths, challenges, forecasts, and remedies with smooth visual effects.

Customization
Modify LLM prompt templates in /backend/utils/prompt_builder.py.

Change GSAP animation settings in /frontend/src/components/animations/.

Adjust static assets and styles under /static and frontend styles folder.

Extend backend API endpoints or add new ones with FastAPI.

Troubleshooting & Tips
Ensure FastAPI backend is running before the frontend to avoid API request failures.

Verify LLM API keys and endpoint URLs are correctly configured in .env.

Confirm GSAP is installed in the frontend and animation hooks are properly wired.

Static files must be correctly referenced in Jinja2 templates for CSS/JS to load.
