from sqlalchemy import create_engine
from dotenv import dotenv_values


def get_database_conn():
    # Get database credentials from environment variable
    config = dict(dotenv_values('.env\.env'))
    print(config)
    db_user_name = config.get('DB_USER_NAME')
    db_password = config.get('DB_PASSWORD')
    db_name = config.get('DB_NAME')
    port = config.get('PORT')
    print(db_user_name)
    host = config.get('HOST')
    # Create and return a postgresql database connection object
    return create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')


def load_data(data):
    engine = get_database_conn()
    data.to_sql('goalBet', con= engine, if_exists='replace', index= False)
    print('Data successfully written to PostgreSQL database')


get_database_conn()