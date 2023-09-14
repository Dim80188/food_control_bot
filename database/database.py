import asyncpg


# вытащить номер аккаунта из таблицы accounts и передать в запрос
class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector


