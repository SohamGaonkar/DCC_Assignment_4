import pandas as pd
import mysql.connector

DB_USER = 'root'
DB_PASSWORD = '1234'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'DCC_Assignment_4'

# To create a database in the local instance  of MySQL
def create_database():
    
    connection = mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = connection.cursor()
    # Creates a database if the databse with the name doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    connection.close()
create_database()


from sqlalchemy import create_engine
# For connecting the database with the flask code
connection_string = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string, echo=True)


df = pd.read_csv("csv_data/EB_Redemption_Details.csv")
df.to_sql(name="redemption_details", con=connection_string, if_exists='replace', index=False)

df = pd.read_csv("csv_data/EB_Purchase_Details.csv")
df.to_sql(name="purchase_details", con=connection_string, if_exists='replace', index=False)

print("CSV files loaded into MySQL tables successfully!")