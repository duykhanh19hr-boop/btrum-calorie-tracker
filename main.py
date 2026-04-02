"""
FastAPI Calorie Tracker Application
Main application file with routes and API endpoints
"""
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json

# Import database and models
from database import engine, Base, SessionLocal, get_db, init_db
from models import User, Food, CalorieLog

# Import schemas
from schemas import CalculationRequest, CalculationResponse, CalorieLogCreate

# Import services
from services.calorie import calculate_bmr, calculate_tdee, calculate_calorie_target
from services.exercise import (
    calories_to_running_km,
    calories_to_walking_minutes,
    calories_to_gym_minutes
)
from services.food_service import calculate_food_calories, get_food_list, load_foods


# Initialize database tables (drop and recreate to ensure schema matches models)
init_db()

# Initialize FastAPI app
app = FastAPI(title="Calorie Tracker", version="1.0.0")

# Set up static files and templates
static_dir = Path(__file__).parent / "static"
templates_dir = Path(__file__).parent / "templates"

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(templates_dir))


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Render the main page with the form
    """
    # Get list of foods to populate dropdown
    foods = get_food_list()
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"foods": foods}
    )


@app.post("/calculate")
async def calculate(request: CalculationRequest) -> CalculationResponse:
    """
    Process calculation request and return results
    
    Calculates:
    - BMR (Basal Metabolic Rate)
    - TDEE (Total Daily Energy Expenditure)
    - Daily calorie target based on goal
    - Calories in selected food
    - Exercise equivalents (running, walking, gym)
    """
    try:
        # Validate inputs
        if request.weight <= 0 or request.height <= 0 or request.age <= 0:
            raise HTTPException(status_code=400, detail="Weight, height, and age must be positive")
        
        if request.quantity < 0:
            raise HTTPException(status_code=400, detail="Quantity must be non-negative")
        
        # Calculate BMR
        bmr = calculate_bmr(
            sex=request.sex,
            weight=request.weight,
            height=request.height,
            age=request.age
        )
        
        # Calculate TDEE
        tdee = calculate_tdee(bmr, request.activity_level)
        
        # Calculate calorie target
        calorie_target = calculate_calorie_target(tdee, request.goal)
        
        # Calculate food calories
        try:
            food_calories = calculate_food_calories(request.food_name, request.quantity)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        # Calculate exercise equivalents
        running_km = calories_to_running_km(food_calories, request.weight)
        walking_minutes = calories_to_walking_minutes(food_calories, request.weight)
        gym_minutes = calories_to_gym_minutes(food_calories, request.weight)
        
        # Save calculation to database
        db = SessionLocal()
        try:
            calorie_log = CalorieLog(
                nickname=request.nickname,
                sex=request.sex,
                age=request.age,
                height=request.height,
                weight=request.weight,
                activity_level=request.activity_level,
                goal=request.goal,
                food_name=request.food_name,
                quantity=request.quantity,
                bmr=bmr,
                tdee=tdee,
                calorie_target=calorie_target,
                food_calories=food_calories,
                exercise_running_km=running_km,
                exercise_walking_minutes=walking_minutes,
                exercise_gym_minutes=gym_minutes
            )
            db.add(calorie_log)
            db.commit()
            db.refresh(calorie_log)
        finally:
            db.close()
        
        # Return results
        return CalculationResponse(
            bmr=bmr,
            tdee=tdee,
            calorie_target=calorie_target,
            food_calories=food_calories,
            exercise_running_km=running_km,
            exercise_walking_minutes=walking_minutes,
            exercise_gym_minutes=gym_minutes
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@app.get("/api/foods")
async def get_foods():
    """
    API endpoint to get list of available foods
    """
    foods = get_food_list()
    return {"foods": foods}


@app.get("/api/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "ok", "message": "Calorie Tracker is running"}


if __name__ == "__main__":
    import uvicorn
    # Run the app with: uvicorn main:app --reload
    uvicorn.run(app, host="127.0.0.1", port=8000)
