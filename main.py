from etl import extract,transform
from util import load_data
from sqlalchemy import create_engine
from dotenv import dotenv_values


extract()
finaldataframe = transform()
print(finaldataframe)
load_data(finaldataframe)