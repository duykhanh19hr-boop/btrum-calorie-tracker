# 🏃 Calorie Tracker - FastAPI Application

A beginner-friendly web application to track calories and calculate daily energy expenditure, built with FastAPI.

## 📋 Project Structure

```
calorie_app/
├── main.py                      # Main FastAPI application
├── database.py                  # SQLAlchemy database configuration
├── models.py                    # SQLAlchemy models (User, Food, CalorieLog)
├── schemas.py                   # Pydantic validation schemas
├── requirements.txt             # Python dependencies
├── services/
│   ├── __init__.py
│   ├── calorie.py              # BMR, TDEE, calorie target calculations
│   ├── exercise.py             # Exercise conversion functions
│   └── food_service.py         # Food data loading and calorie calculations
├── templates/
│   └── index.html              # Main HTML template with form and results
├── static/
│   └── style.css               # Custom CSS styling
└── data/
    └── foods.json              # Sample food database with calorie data
```

## 🎯 Features

- **User Profile Management**: Input height, weight, age, sex, and activity level
- **BMR Calculation**: Basal Metabolic Rate using Mifflin-St Jeor equation
- **TDEE Calculation**: Total Daily Energy Expenditure based on activity level
- **Daily Target**: Personalized calorie target based on fitness goal
- **Food Database**: 20+ pre-loaded foods with calorie information
- **Exercise Conversion**: Convert food calories to:
  - Running distance (km)
  - Walking duration (minutes)
  - Gym workout duration (minutes)
- **Responsive Design**: Bootstrap UI that works on desktop and mobile
- **No AI API Required**: All calculations are local and privacy-friendly

## 🛠️ Installation & Setup

### Step 1: Install Python
Ensure you have Python 3.8 or higher installed on your system.

### Step 2: Navigate to Project Directory
Open Command Prompt and navigate to the project folder:
```bash
cd "D:\office\OneDrive\Desktop\Aptech\Python\PYTHON BASIC\python tự học\calorie_app"
```

### Step 3: Create Virtual Environment
Create and activate a Python virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# On Mac/Linux:
# source venv/bin/activate
```

### Step 4: Install Dependencies
Install required packages:
```bash
pip install -r requirements.txt
```

### Step 5: Initialize Database
Create the SQLite database:
```bash
python -c "from database import engine, Base; Base.metadata.create_all(bind=engine)"
```

## 🚀 Running the Application

### Start the Development Server
```bash
uvicorn main:app --reload
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

### Access the Application
Open your web browser and go to:
```
http://127.0.0.1:8000
```

## 📖 How to Use

1. **Fill in Your Information**:
   - Enter your nickname
   - Select your sex (Male/Female)
   - Enter your age, height (cm), and weight (kg)
   - Select your activity level
   - Choose your fitness goal (Lose/Maintain/Gain weight)

2. **Select Food & Quantity**:
   - Choose a food item from the dropdown
   - Enter the quantity in grams (default: 100g)

3. **Calculate Results**:
   - Click "Calculate Results" button
   - View your personalized calorie metrics and exercise equivalents

## 🧮 Calculation Methods

### BMR (Basal Metabolic Rate)
Using Mifflin-St Jeor equation:
- **Men**: (10 × weight) + (6.25 × height) - (5 × age) + 5
- **Women**: (10 × weight) + (6.25 × height) - (5 × age) - 161

### TDEE (Total Daily Energy Expenditure)
TDEE = BMR × Activity Multiplier
- Sedentary: 1.2
- Lightly Active: 1.375
- Moderately Active: 1.55
- Very Active: 1.725

### Daily Calorie Target
- **Lose Weight**: TDEE - 500 calories
- **Maintain**: TDEE calories
- **Gain Weight**: TDEE + 500 calories

### Exercise Conversions
Estimates based on average 70kg person (adjusted for actual weight):
- **Running**: ~60 calories/km at 8 km/h pace
- **Walking**: ~4 calories/minute at moderate pace
- **Gym Workout**: ~6 calories/minute (cardio + strength mix)

## 📝 Available Foods

The app comes with 20 pre-loaded foods:
- Fruits: Apple, Banana, Orange
- Proteins: Chicken Breast, Salmon, Beef, Pork, Egg
- Grains: Brown Rice, White Bread, Pasta
- Vegetables: Broccoli, Carrot, Potato, Spinach
- Dairy: Milk, Yogurt, Cheese
- Healthy Fats: Almond, Olive Oil

You can add more foods by editing `data/foods.json`.

## 🔧 Adding More Foods

Edit `data/foods.json` and add new items:
```json
{
    "name": "Food Name",
    "calories_per_100g": 150
}
```

## 📊 API Endpoints

- `GET /` - Main HTML page
- `POST /calculate` - Calculate calories and metrics
- `GET /api/foods` - Get list of available foods
- `GET /api/health` - Health check endpoint

## 🗄️ Database Tables

The app automatically creates these SQLite tables:
- **users** - User profiles
- **foods** - Food database
- **calorie_logs** - User calorie intake history

## 🐛 Troubleshooting

### "Module not found" error
Make sure your virtual environment is activated and all dependencies are installed:
```bash
pip install -r requirements.txt
```

### "Address already in use" error
The port 8000 is already in use. Run on a different port:
```bash
uvicorn main:app --reload --port 8001
```

### "foods.json not found" error
Make sure the `data/foods.json` file exists in the correct location.

## 📚 Code Comments

The code includes detailed comments explaining:
- Function purposes and parameters
- Calculation methods and equations
- API endpoint behavior
- HTML form structure and JavaScript functionality

Great for learning FastAPI, SQLAlchemy, and web development!

## 🎓 Learning Resources

This project demonstrates:
- FastAPI REST API development
- Jinja2 templating
- SQLAlchemy ORM
- Pydantic data validation
- HTML/CSS/JavaScript frontend
- Database operations with SQLite
- RESTful API design patterns

## 💡 Future Improvements

- User authentication (login/signup)
- Save and view past logs
- Meal planning features
- Advanced nutrition tracking
- Mobile app version
- Export reports as PDF

## 📄 License

This is an educational project. Feel free to modify and use it for learning purposes.

## ❓ Questions?

Refer to the code comments for detailed explanations of how each component works. Happy coding! 🎉
