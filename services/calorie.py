"""
Calorie calculation services
Functions for BMR, TDEE, and calorie target calculations
"""


def calculate_bmr(sex: str, weight: float, height: float, age: int) -> float:
    """
    Calculate Basal Metabolic Rate (BMR) using Mifflin-St Jeor equation
    
    Args:
        sex: "Male" or "Female"
        weight: weight in kg
        height: height in cm
        age: age in years
    
    Returns:
        BMR in calories per day
    """
    if sex.lower() == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:  # Female
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    return round(bmr, 2)


def calculate_tdee(bmr: float, activity_level: str) -> float:
    """
    Calculate Total Daily Energy Expenditure (TDEE) based on activity level
    
    Args:
        bmr: Basal Metabolic Rate
        activity_level: One of "sedentary", "lightly_active", "moderately_active", "very_active"
    
    Returns:
        TDEE in calories per day
    """
    # Activity multipliers
    activity_multipliers = {
        "sedentary": 1.2,              # Little to no exercise
        "lightly_active": 1.375,       # Exercise 1-3 days per week
        "moderately_active": 1.55,     # Exercise 3-5 days per week
        "very_active": 1.725,          # Exercise 6-7 days per week
    }
    
    multiplier = activity_multipliers.get(activity_level.lower(), 1.2)
    tdee = bmr * multiplier
    
    return round(tdee, 2)


def calculate_calorie_target(tdee: float, goal: str) -> float:
    """
    Calculate daily calorie target based on fitness goal
    
    Args:
        tdee: Total Daily Energy Expenditure
        goal: One of "lose", "maintain", "gain"
    
    Returns:
        Daily calorie target
    """
    if goal.lower() == "lose":
        # Deficit of 500 calories per day (safe weight loss)
        target = tdee - 500
    elif goal.lower() == "gain":
        # Surplus of 500 calories per day (safe weight gain)
        target = tdee + 500
    else:  # maintain
        target = tdee
    
    return round(target, 2)
