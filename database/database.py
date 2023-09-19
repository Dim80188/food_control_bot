import asyncpg


# вытащить номер аккаунта из таблицы accounts и передать в запрос
class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def get_user_id(self, tg_id):
        tg_id_1 = tg_id
        user_id = await self.connector.fetch("SELECT id FROM accounts WHERE id_telegram = $1", tg_id_1)
        return user_id[0][0]

    async def add_meal(self, data):
        await self.connector.execute("INSERT INTO meal (user_id, date_meal, product_name, weight) VALUES ($1, $2, $3, $4)",
                                     data['user_id'], data['date_meal'], data['name'], int(data['weight']))


