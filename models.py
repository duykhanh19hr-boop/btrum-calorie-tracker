"""
SQLAlchemy models for the application
"""
from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime


class User(Base):
    """
    User model to store user profile information
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, unique=True, index=True)
    sex = Column(String)  # "Male" or "Female"
    age = Column(Integer)
    height = Column(Float)  # in cm
    weight = Column(Float)  # in kg
    activity_level = Column(String)  # "sedentary", "lightly_active", "moderately_active", "very_active"
    goal = Column(String)  # "lose", "maintain", "gain"
    created_at = Column(DateTime, default=datetime.utcnow)


class Food(Base):
    """
    Food model to store food items
    """
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    calories_per_100g = Column(Float)  # Calories per 100g


class CalorieLog(Base):
    """
    CalorieLog model to store user calorie intake logs and calculations
    """
    __tablename__ = "calorie_logs"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String)
    sex = Column(String)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    activity_level = Column(String)
    goal = Column(String)
    food_name = Column(String)
    quantity = Column(Float)  # in grams
    bmr = Column(Float)
    tdee = Column(Float)
    calorie_target = Column(Float)
    food_calories = Column(Float)
    exercise_running_km = Column(Float)
    exercise_walking_minutes = Column(Float)
    exercise_gym_minutes = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
