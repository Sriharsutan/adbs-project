from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "user1",
    "password": "user1!23",
    "database": "social_media_dashboard"
}
@app.route('/instagram')
def instagram():
    print("Fetching Instagram data...")
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    
    query = "SELECT * FROM new_instagram_posts_3 LIMIT 9"
    cursor.execute(query)
    posts = cursor.fetchall()
    
    cursor.close()
    connection.close()

    print("Instagram data fetched successfully.")
    
    return render_template('instagram_page.html', posts=posts)


# @app.route('/instagram')
# def instagram():
#     posts = [
#         [1, "Nice post!", 101, 202, "2024-11-20", "https://example.com/image.jpg", 102, "2024-11-21"],
#         [2, "Awesome!", 103, 203, "2024-11-19", "https://example.com/image2.jpg", 104, "2024-11-20"]
#     ]
#     return render_template('instagram_page.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
