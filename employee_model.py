from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length = 3, max_length = 50, description="Employee's full name", example="John Doe")
    department: Optional[str] = 'General'
    salary: float = Field(..., gt=0, description="Employee's salary", example=50000.00)

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="Username for the employee", example="johndoe")
    email: str = Field(..., regex=r'^\S+@\S+\.\S+$', description="Employee's email address", example=" 