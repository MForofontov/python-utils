"""Calculate age from a birth date."""

from datetime import datetime, date
from typing import Union


def calculate_age(birth_date: Union[datetime, date], reference_date: Union[datetime, date] = None) -> int:
    """
    Calculate age in years from a birth date.
    
    Args:
        birth_date: The birth date
        reference_date: The reference date to calculate age against (default: today)
        
    Returns:
        Age in years
        
    Raises:
        TypeError: If birth_date is not a datetime or date object
        ValueError: If birth_date is in the future
    """
    if not isinstance(birth_date, (datetime, date)):
        raise TypeError("birth_date must be a datetime or date object")
    
    if reference_date is None:
        reference_date = date.today()
    elif not isinstance(reference_date, (datetime, date)):
        raise TypeError("reference_date must be a datetime or date object")
    
    # Convert to date objects for comparison
    if isinstance(birth_date, datetime):
        birth_date = birth_date.date()
    if isinstance(reference_date, datetime):
        reference_date = reference_date.date()
    
    if birth_date > reference_date:
        raise ValueError("birth_date cannot be in the future")
    
    # Calculate age
    age = reference_date.year - birth_date.year
    
    # Check if birthday has occurred this year
    if (reference_date.month, reference_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age
