import pandas as pd
import mysql.connector

# Load the data
df = pd.read_csv("timesjobs_data.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",  # replace this
    database="job_data"              # make sure this DB exists
)
cursor = conn.cursor()

# Insert into MySQL
for _, row in df.iterrows():
    sql = """
    INSERT INTO job_listings (title, company, location, skills, date_posted)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (row['title'], row['company'], row['location'], row['skills'], row['date_posted'])
    cursor.execute(sql, values)

conn.commit()
print("✅ Data inserted successfully!")

cursor.close()
conn.close()
