from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client['car_ocr']
users = db['users']
records = db['records']
print("Connected to DB")