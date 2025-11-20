from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ajouter le port :5432
SQLALCHEMY_DATABASE_URL = "postgresql://saifridenetek:SEPTSEGh12!@database-1.czk6k8cycan4.us-east-1.rds.amazonaws.com:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
