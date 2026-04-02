"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    """Base schema for User"""
    nickname: str
    sex: str
    age: int
    height: float
    weight: float
    activity_level: str
    goal: str


class UserCreate(UserBase):
    """Schema for creating a user"""
    pass


class User(UserBase):
    """Schema for reading user data"""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FoodBase(BaseModel):
    """Base schema for Food"""
    name: str
    calories_per_100g: float


class FoodCreate(FoodBase):
    """Schema for creating a food"""
    pass


class Food(FoodBase):
    """Schema for reading food data"""
    id: int

    model_config = ConfigDict(from_attributes=True)


class CalorieLogBase(BaseModel):
    """Base schema for CalorieLog"""
    nickname: str
    sex: str
    age: int
    height: float
    weight: float
    activity_level: str
    goal: str
    food_name: str
    quantity: float
    bmr: float
    tdee: float
    calorie_target: float
    food_calories: float
    exercise_running_km: float
    exercise_walking_minutes: float
    exercise_gym_minutes: float


class CalorieLogCreate(CalorieLogBase):
    """Schema for creating a calorie log"""
    pass


class CalorieLog(CalorieLogBase):
    """Schema for reading calorie log data"""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CalculationRequest(BaseModel):
    """Schema for calculation request"""
    nickname: str
    sex: str
    age: int
    height: float
    weight: float
    activity_level: str
    goal: str
    food_name: str
    quantity: float


class CalculationResponse(BaseModel):
    """Schema for calculation response"""
    bmr: float
    tdee: float
    calorie_target: float
    food_calories: float
    exercise_running_km: float
    exercise_walking_minutes: float
    exercise_gym_minutes: float
