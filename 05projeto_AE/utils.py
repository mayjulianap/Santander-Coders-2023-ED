from sqlalchemy import text as sql_text
from sqlalchemy.schema import CreateSchema

def create_schemas(engine, schema_name):
    create_schema_sql = sql_text(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
    try:
        with engine.connect() as connection:
            connection.execute(CreateSchema(f"{schema_name}", if_not_exists=True))
            connection.commit()
            print("Schema created successfully.")
    except Exception as e:
        print(f"Failed to create schema: {e}")