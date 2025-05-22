# Trader
1. Create a .env file with database connection details:

SQLALCHEMY_WARN_20=0

SQLALCHEMY_SILENCE_UBER_WARNING=1

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/trader_api

API_HOST=localhost

API_PORT=8000

SECRET_KEY=your-super-secret-key-change-this-in-production

DEFAULT_TIMEFRAME=1h

MAX_POSITIONS=10
