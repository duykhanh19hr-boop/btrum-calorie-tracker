"""
Database configuration for SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Create SQLite database with absolute path
DATABASE_URL = "sqlite:///./calorie_app.db"

# Create engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def init_db():
    """
    Initialize database by dropping and recreating all tables.
    Use this to ensure schema matches the current SQLAlchemy models.
    """
    # Drop all existing tables
    Base.metadata.drop_all(bind=engine)
    # Create all tables
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Dependency function to get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
