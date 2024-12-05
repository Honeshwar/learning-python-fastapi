from pydantic import BaseModel, Field,  field_validator
from typing import Literal,Optional

class AddTeamLeader(BaseModel):
    # String fields with minimum and maximum length validations
    first_name: str = Field(..., min_length=3, max_length=200, description="First name must be between 3 and 200 characters.")
    last_name: str = Field(..., min_length=3, max_length=200, description="Last name must be between 3 and 200 characters.")
    
    # Gender field limited to specific values (using Literal)
    gender: Literal["Male", "Female", "Other"] = Field(..., description="Gender must be 'Male', 'Female', or 'Other'.")
    
    # Mobile number with regex for validation
    mobile: str = Field(..., pattern=r"^[6-9]\d{9}$", description="Mobile number must be a valid 10-digit number starting with 6, 7, 8, or 9.")
    
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", description="Email must be a valid email address.")
    # Graduation year must be between a valid range (e.g., 1900 and the current year)
    graduation_year: int = Field(..., ge=1900, le=2100, description="Graduation year must be between 1900 and 2100.")
    
    # College name with minimum and maximum length validation
    college_name: str = Field(..., min_length=3, max_length=200, description="College name must be between 3 and 200 characters.")
    
    # State and zone validation with string lengths
    state: str = Field(..., min_length=2, max_length=100, description="State name must be between 2 and 100 characters.")
    zone: str = Field(..., min_length=2, max_length=100, description="Zone name must be between 2 and 100 characters.")
    checkbox1: Optional[bool] = 0
    checkbox2: Optional[bool] = 0
    
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_campaign: Optional[str] = None

    
    # Custom validator for ensuring the mobile number starts with a valid digit
    # @field_validator("mobile")
    # def validate_mobile(cls, value):
    #     if str(value)[0] not in "6789":
    #         raise ValueError("Mobile number must start with 6, 7, 8, or 9.")
    #     return value
    
    # Graduation year dynamic validator based on the current year
    @field_validator("graduation_year")
    def validate_graduation_year(cls, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError(f"Graduation year cannot be in the future (after {current_year}).")
        return value
