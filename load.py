import pandas as pd
import pymysql
from pymysql import Error

# Read the CSV file using pandas
csv_file_path = '/home/sutan/Documents/adb-project/mergerd.csv'  # Adjust the path to your file
df = pd.read_csv(csv_file_path)

# Drop rows with NaN values (if needed)
#df = df.dropna(subset=['id', 'comment_text', 'user_id_x', 'photo_id', 'created_at', 'image_url', 'user_id_y', 'created_dat'])

# Connect to MySQL
try:
    connection = pymysql.connect(
        host='localhost',        # Your MySQL host
        database='social_media_dashboard',  # Your MySQL database name
        user='user1',            # Your MySQL username
        password='user1!23'      # Your MySQL password
    )

    if connection.open:
        print("Successfully connected to MySQL database")

        # Create a cursor object
        cursor = connection.cursor()

        # Create table if not exists
        create_table_query = """
        CREATE TABLE IF NOT EXISTS new_instagram_posts_3 (
            id INT PRIMARY KEY,
            comment_text TEXT,
            user_id_x INT,
            photo_id INT,
            created_at DATETIME,
            image_url VARCHAR(255),
            user_id_y INT,
            created_dat DATETIME
        );
        """
        cursor.execute(create_table_query)
        print("Table created or already exists.")

        # Insert data into the table
        insert_query = """
        INSERT INTO new_instagram_posts_3 (
            id, comment_text, user_id_x, photo_id, created_at, image_url, user_id_y, created_dat
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        for index, row in df.iterrows():
            try:
                # Prepare row values
                row_values = (
                    row['id'], row['comment_text'], row['user_id_x'], 
                    row['photo_id'], row['created_at'], row['image_url'], 
                    row['user_id_y'], row['created_dat']
                )
                print(f"Inserting row {index} with data: {row_values}")  # Debugging
                cursor.execute(insert_query, row_values)
            except Exception as e:
                print(f"Error inserting row {index}: {e}")
                print(f"Row data: {row_values}")  # Show the problematic row data

        # Commit the transaction
        connection.commit()
        print(f"Inserted {len(df)} rows into the database.")

except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if connection.open:
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
