##utility tools
from datetime import datetime

def get_todays_date() -> str:
    """Get todays date """
    return datetime.now().strftime("%Y-%m-%d")

def get_todays_date_and_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%m")
