import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pymysql
from pymysql import Error

connection = pymysql.connect(
        host='localhost',        # Your MySQL host
        database='social_media_dashboard',  # Your MySQL database name
        user='user1',    # Your MySQL username
        password='user1!23' # Your MySQL password
    )
# Sample query to fetch data from MySQL
query = "SELECT likes, num_comments FROM new_instagram_posts_1"
df = pd.read_sql(query, connection)

# Create a scatter plot
sns.scatterplot(x='num_comments', y='likes', data=df)
plt.title('Likes vs. Number of Comments')
plt.show()
