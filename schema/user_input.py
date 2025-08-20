from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

class user_input(BaseModel):
    age: Annotated[int, Field(...,gt=0, le=120,discription="Age of the user, must be between 1 and 120")]
    weight: Annotated[float, Field(...,gt=0, le=150, description="Weight of the user in kg, must be between 0.1 and 150 kg")]
    height: Annotated[float, Field(...,gt=0, le=2.5, description="Height of the user in meters")]
    income_lpa: Annotated[float, Field(...,gt=0, le=100, description="Income of the user in lakhs per annum, must be between 0.1 and 100 LPA")]
    smoker: Annotated[bool, Field(...,description="Whether the user is a smoker or not")]
    city: Annotated[str, Field(...,max_length=100, description="City of the user, must be a string with a maximum length of 100 characters")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    
    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate Body Mass Index (BMI)"""
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        """Determine lifestyle risk based on smoking status and BMI"""
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    
    
    @computed_field
    @property
    def age_group(self) -> str:
        """Determine age group based on age"""
        if self.age < 18:
            return "Minor"
        elif 18 <= self.age < 60:
            return "Adult"
        else:
            return "Senior"
        
    @computed_field
    @property
    def city_tier(self) -> str:
        """Determine city tier based on city name"""
        if self.city in tier_1_cities:
            return "Tier 1"
        elif self.city in tier_2_cities:
            return "Tier 2"
        else:
            return "Tier 3"