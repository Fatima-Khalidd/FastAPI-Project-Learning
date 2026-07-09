from dotenv import load_dotenv
import os 

load_dotenv()
class Settings:
    SECRET_KEY=os.getenv("SECRET_KEY")  # using "SECRET_KEY" value from .env file
    DB_URL=os.getenv("DB_URL") # Using 'DB_URL' value from  .env file


settings=Settings()