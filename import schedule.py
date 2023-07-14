import schedule
import time
import mysql.connector

def records():
    try:
        conn = mysql.connector.connect(database="schedule",
                                       user="root",
                                       password="Nithin@2003",
                                       host="localhost",
                                       port="3306")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM time")
        records = cursor.fetchall()
        for row in records:
            print(row)
        conn.close()
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)

# Schedule the task
schedule.every().day.at("10:44").do(records)
schedule.every().day.at("10:45").do(records)

# Keep the program running
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        break