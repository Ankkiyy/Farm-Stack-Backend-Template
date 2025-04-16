import os
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load development environment if ENVIRONMENT is set to development
if os.getenv('ENVIRONMENT') == 'development':
    load_dotenv('.env.development')
else:
    load_dotenv()

DB_TYPE = os.getenv('DB_TYPE', 'mongodb')  # Default to MongoDB if not set

# Initialize variables as None
client = None
db = None
session = None

isMySqlAvailable = False
isMongoDBAvailable = False

if DB_TYPE in ['mongodb', 'both']:
    MONGO_SERVER_URL = os.getenv('MONGO_SERVER_URL', 'mongodb://localhost:27017')
    MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'template')
    # Initialize MongoDB connection
    client = MongoClient(MONGO_SERVER_URL)
    db = client[MONGO_DB_NAME]
    isMongoDBAvailable=True

if DB_TYPE in ['mysql', 'both']:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')
    MYSQL_USER = os.getenv('MYSQL_USER', 'user')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
    MYSQL_DB_NAME = os.getenv('MYSQL_DB_NAME', 'dbname')

    MYSQL_SERVER_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}"
    engine = create_engine(MYSQL_SERVER_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    isMySqlAvailable=True

    # Example: Define tables or ORM models here if needed
    # from .models import Base
    # Base.metadata.create_all(engine)

if DB_TYPE not in ['mongodb', 'mysql', 'both']:
    raise ValueError("Unsupported DB_TYPE. Please set DB_TYPE to 'mongodb', 'mysql', or 'both'.")