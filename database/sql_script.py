CREATE_ACCOUNTS_TABLE = \
    """
    CREATE TABLE IF NOT EXISTS accounts(
        id SERIAL NOT NULL PRIMARY KEY,
        id_telegram BIGINT,
        user_name TEXT
        );
    """
CREATE_MEAL_TABLE = \
    """
    CREATE TABLE IF NOT EXISTS meal(
        id SERIAL NOT NULL PRIMARY KEY,
        user_id BIGINT,
        date_meal DATE,
        product_name TEXT,
        weight REAL,
        CONSTRAINT fk FOREIGN KEY (user_id) REFERENCES accounts (id)
        );
    """
CREATE_PRODUCTS_TABLE = \
    """
        CREATE TABLE IF NOT EXISTS products(
        id SERIAL NOT NULL PRIMARY KEY,
        name TEXT,
        calories REAL,
        proteins REAL,
        fat REAL,
        carbon REAL,
        v_a REAL,
        v_b_1 REAL,
        v_b_2 REAL,
        v_b_4 REAL,
        v_b_5 REAL,
        v_b_6 REAL,
        v_b_9 REAL,
        v_b_12 REAL,
        v_c REAL,
        v_d REAL,
        v_e REAL,
        v_k REAL,
        v_pp REAL,
        k REAL,
        ca REAL,
        mg REAL,
        na REAL,
        s REAL,
        p REAL,
        fe REAL,
        i REAL,
        cu REAL,
        se REAL,
        zn REAL
        );
    """