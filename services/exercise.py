"""
Exercise conversion services
Convert calories to equivalent exercise distances/durations
"""


def calories_to_running_km(calories: float, weight: float) -> float:
    """
    Convert calories burned to equivalent kilometers of running
    
    Assumption: Running at moderate pace (8 km/h) burns approximately 60 calories per km per 70kg person
    
    Args:
        calories: calories to burn
        weight: user weight in kg
    
    Returns:
        Distance in km needed to burn the calories
    """
    # Calories per km adjusted for weight (lean body burns more calories)
    # Base: 60 cal/km for 70kg person
    base_weight = 70
    calories_per_km = 60 * (weight / base_weight)
    
    km = calories / calories_per_km
    return round(km, 2)


def calories_to_walking_minutes(calories: float, weight: float) -> float:
    """
    Convert calories burned to equivalent minutes of walking
    
    Assumption: Walking at moderate pace (5 km/h) burns approximately 4 calories per minute per 70kg person
    
    Args:
        calories: calories to burn
        weight: user weight in kg
    
    Returns:
        Duration in minutes needed to burn the calories
    """
    # Calories per minute adjusted for weight
    # Base: 4 cal/min for 70kg person
    base_weight = 70
    calories_per_minute = 4 * (weight / base_weight)
    
    minutes = calories / calories_per_minute
    return round(minutes, 2)


def calories_to_gym_minutes(calories: float, weight: float) -> float:
    """
    Convert calories burned to equivalent minutes of gym workout
    
    Assumption: Moderate gym workout (mix of cardio and strength) burns approximately 6 calories per minute per 70kg person
    
    Args:
        calories: calories to burn
        weight: user weight in kg
    
    Returns:
        Duration in minutes needed to burn the calories
    """
    # Calories per minute adjusted for weight
    # Base: 6 cal/min for 70kg person
    base_weight = 70
    calories_per_minute = 6 * (weight / base_weight)
    
    minutes = calories / calories_per_minute
    return round(minutes, 2)
