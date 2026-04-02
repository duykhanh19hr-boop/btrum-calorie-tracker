"""
Food service
Load foods from JSON file and calculate calories
"""
import json
import os
from pathlib import Path


def load_foods() -> dict:
    """
    Load foods from foods.json file
    
    Returns:
        Dictionary with food name as key and calories_per_100g as value
    """
    # Get the directory where this file is located
    current_dir = Path(__file__).parent.parent
    foods_file = current_dir / "data" / "foods.json"
    
    try:
        with open(foods_file, 'r', encoding='utf-8') as f:
            foods_data = json.load(f)
        
        # Convert list of foods to dictionary for easier lookup
        foods_dict = {}
        for food in foods_data:
            foods_dict[food["name"]] = food["calories_per_100g"]
        
        return foods_dict
    except FileNotFoundError:
        print(f"Warning: foods.json not found at {foods_file}")
        return {}
    except json.JSONDecodeError:
        print(f"Warning: foods.json is not valid JSON")
        return {}


def get_food_list():
    """
    Get list of all available foods
    
    Returns:
        List of food names
    """
    foods = load_foods()
    return sorted(foods.keys())


def calculate_food_calories(food_name: str, quantity: float) -> float:
    """
    Calculate total calories for a specific food and quantity
    
    Args:
        food_name: Name of the food
        quantity: Quantity in grams
    
    Returns:
        Total calories
    """
    foods = load_foods()
    
    if food_name not in foods:
        raise ValueError(f"Food '{food_name}' not found in database")
    
    calories_per_100g = foods[food_name]
    total_calories = (quantity / 100) * calories_per_100g
    
    return round(total_calories, 2)
