from src.database.models import create_tables, get_engine

if __name__ == "__main__":
    engine = get_engine()
    create_tables(engine)
    print("Database tables created successfully")
