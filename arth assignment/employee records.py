from fastapi import FastAPI, UploadFile, File
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import openai # Or Gemini SDK

app = FastAPI()

# Database Setup 
SQLALCHEMY_DATABASE_URL = "sqlite:///./hrms.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Models ---

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    designation = Column(String)
    department = Column(String)
    joining_date = Column(Date)
    bio = Column(String) # For AI-generated bio 

class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    resume_text = Column(String)
    match_percentage = Column(Float) # AI Score 
    status = Column(String, default="Applied") # [cite: 58]

Base.metadata.create_all(bind=engine)