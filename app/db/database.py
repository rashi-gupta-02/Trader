import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/trader_api")

try:
    # Parse the URL
    import urllib.parse as urlparse
    url = urlparse.urlparse(DATABASE_URL)
    
    conn = psycopg2.connect(
        host=url.hostname,
        port=url.port,
        database=url.path[1:],  # Remove leading '/'
        user=url.username,
        password=url.password
    )
    print("Successfully connected to PostgreSQL!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")