import asyncpg
import asyncio
from database.sql_script import *
from config_data.config import Config, load_config

async def main():
    config: Config = load_config()
    connection = await asyncpg.connect(user=config.db.db_user, password=config.db.db_password,
                                     database=config.db.database, host=config.db.db_host,
                                     port=5432)
    statements = [CREATE_ACCOUNTS_TABLE,
                  CREATE_MEAL_TABLE,
                  CREATE_PRODUCTS_TABLE]

    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    await connection.close()

asyncio.run(main())