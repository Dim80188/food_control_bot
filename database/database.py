import asyncpg


# вытащить номер аккаунта из таблицы accounts и передать в запрос
class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_user(self, tg_id):
        tg_id_1 = tg_id
        await self.connector.fetch("INSERT INTO accounts (id_telegram) SELECT $1 WHERE NOT EXISTS (SELECT id_telegram FROM accounts WHERE id_telegram = $1)", tg_id_1)

    async def get_user_id(self, tg_id):
        tg_id_1 = tg_id
        user_id = await self.connector.fetch("SELECT id FROM accounts WHERE id_telegram = $1", tg_id_1)
        return user_id[0][0]

    async def add_meal(self, data):
        await self.connector.execute("INSERT INTO meal (user_id, date_meal, product_name, weight) VALUES ($1, $2, $3, $4)",
                                     data['user_id'], data['date_meal'], data['name'], (float(data['weight'])/100))


    async def get_meal(self, data):
        await self.connector.execute("SELECT calories, proteins FROM products, meal WHERE products.name = $1 AND meal.product_name = $1",
                                     data['product'])

    async def sql_read(self, period, period_id):
        sql_id = period_id
        sql_start = period['start_period']
        sql_end = period['end_period']
        ret = await self.connector.fetch(f"SELECT product_name, products.calories * meal.weight AS calories, products.proteins * meal.weight AS proteins, products.carbon * meal.weight AS carbon, products.fat * meal.weight AS fat FROM accounts, meal, products WHERE accounts.id = meal.user_id AND products.name = meal.product_name AND meal.date_meal BETWEEN $1 AND $2 AND accounts.id_telegram = $3",
                                         sql_start, sql_end, sql_id)

        return ret

    async def total_data(self, ret):
        counter = 0
        total_list = []
        for i in range(1, len(ret[0])):
            counter = 0
            for j in range(len(ret)):
                counter += ret[j][i]
            total_list.append(counter)
        return total_list

    async def sql_read_one_day(self, period, period_id):
        sql_id = period_id
        sql_date = period['day_deletion_data']
        ret = await self.connector.fetch(f"SELECT * FROM meal WHERE user_id = $1 AND date_meal = $2", sql_id, sql_date)
        return ret

    async def sql_delete_command(self, id):
        id_1 = id
        await self.connector.execute('DELETE FROM meal WHERE id = $1', id_1)


# a = [[1, 2, 3, 4], [2, 4, 5, 1], [9, 4, 2, 0]]
# b = []
# c = 0
# d = 0
# for i in range(len(a[0])):
#     c = 0
#     for j in range(len(a)):
#         c += a[j][i]
#     b.append(c)


