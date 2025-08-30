from sqlalchemy import create_engine


# need to hide DB credentials with .env file or use other ways to hide them
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)
