import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key(key_name):
  key=os.getenv(key_name)
  if not key:
    raise ValueError(f"{key_name} not found in env variables please check the variable /key name")
  return key