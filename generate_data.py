import pandas as pd
import random
import string
from datetime import datetime, timedelta

# Define the columns
columns = [
    "url", "user_posted", "description", "hashtags", "num_comments", "date_posted",
    "likes", "photos", "videos", "location", "latest_comments", "post_id", 
    "discovery_input", "has_handshake", "display_url", "shortcode", "content_type", 
    "pk", "content_id", "engagement_score_view", "thumbnail", "video_view_count", 
    "product_type", "coauthor_producers", "tagged_users", "video_play_count", 
    "followers", "posts_count", "profile_image_link", "is_verified", 
    "is_paid_partnership", "partnership_details", "user_posted_id", "post_content", 
    "audio", "profile_url"
]

# Function to generate random data for each column
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_date(start_date, days=365):
    return start_date + timedelta(days=random.randint(0, days))

# Generate data
data = []
for i in range(100):  # Generate 100 rows
    row = {
        "url": f"https://example.com/post/{random_string(5)}",
        "user_posted": random_string(8),
        "description": f"Post description {i}",
        "hashtags": f"#tag{random.randint(1, 100)}",
        "num_comments": random.randint(0, 500),
        "date_posted": random_date(datetime(2020, 1, 1), 1000).strftime('%Y-%m-%d %H:%M:%S'),
        "likes": random.randint(0, 10000),
        "photos": random.randint(0, 5),
        "videos": random.randint(0, 2),
        "location": f"Location {random.randint(1, 50)}",
        "latest_comments": f"Comment {random.randint(1, 200)}",
        "post_id": i + 1,
        "discovery_input": random_string(15),
        "has_handshake": random.choice([True, False]),
        "display_url": f"https://example.com/image/{random_string(5)}.jpg",
        "shortcode": random_string(8),
        "content_type": random.choice(["image", "video", "carousel"]),
        "pk": random.randint(1_000_000, 10_000_000),
        "content_id": random.randint(1_000_000, 10_000_000),
        "engagement_score_view": round(random.uniform(0.1, 10.0), 2),
        "thumbnail": f"https://example.com/thumbnail/{random_string(5)}.jpg",
        "video_view_count": random.randint(0, 5000),
        "product_type": random.choice(["organic", "sponsored"]),
        "coauthor_producers": f"User {random.randint(1, 50)}",
        "tagged_users": f"User{random.randint(1, 20)}",
        "video_play_count": random.randint(0, 5000),
        "followers": random.randint(100, 100_000),
        "posts_count": random.randint(1, 500),
        "profile_image_link": f"https://example.com/profile/{random_string(5)}.jpg",
        "is_verified": random.choice([True, False]),
        "is_paid_partnership": random.choice([True, False]),
        "partnership_details": f"Partnership with Brand {random.randint(1, 50)}",
        "user_posted_id": random.randint(1, 100),
        "post_content": f"Content of post {i}",
        "audio": f"Audio clip {random.randint(1, 100)}",
        "profile_url": f"https://example.com/user/{random_string(5)}"
    }
    data.append(row)

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
output_file = "/home/sutan/Documents/adb-project/generated_instagram_dataset.csv"
df.to_csv(output_file, index=False)
print(f"Sample dataset generated and saved as '{output_file}'.")
