from decouple import config as decouple_config
DATABASE_URL = decouple_config('DATABASE_URL',default="postgresql+psycopg://time-user:time-pw@localhost:5432/timescaledb")
DB_TIMEZONE = decouple_config('DB_TIMEZONE',default="UTC")
