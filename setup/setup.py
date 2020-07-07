#! /bin/python3

import subprocess
import sys
import pymongo

print("You need to have pip installed.")
dependencies = ["pandas", "numpy", "sklearn", "keras", "matplotlib",
        "tensorflow"]

# installing packages
for tmp in dependencies:
    subprocess.check_call([sys.executable, "-m", "pip", "install", tmp])


# setting up database
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
stock_db = db_client["stocks"]
stock_hist = stock_db["history"]
