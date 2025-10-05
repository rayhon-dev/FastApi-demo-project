from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite
DATABASE_URL = "sqlite:///./blog.db"

# Agar PostgreSQL ishlatsangiz:
# DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/mydatabase"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # faqat sqlite uchun kerak
)

# Session (DB bilan ishlash uchun)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baza uchun asosiy class
Base = declarative_base()
