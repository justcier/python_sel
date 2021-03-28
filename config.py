import os

from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from .env file located in the same folder as this file
load_dotenv(override=True, verbose=True)

# Credentials
USER_EMAIL = os.getenv('USER_EMAIL')
USER_PASSWORD = os.getenv('USER_PASSWORD')

# Sites
SITE = os.getenv('APP_URL')
BROWSER_CONFIG = os.getenv("BROWSER_CONFIG")