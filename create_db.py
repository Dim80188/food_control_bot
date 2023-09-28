

# CREATE TABLE IF NOT EXISTS accounts
# (
#     id integer NOT NULL DEFAULT nextval('accounts_id_seq'::regclass),
#     id_telegram bigint,
#     user_name text COLLATE pg_catalog."default",
#     CONSTRAINT accounts_pkey PRIMARY KEY (id)
# )
#
# CREATE TABLE IF NOT EXISTS meal
# (
#     id integer NOT NULL DEFAULT nextval('meal_id_seq'::regclass),
#     user_id bigint,
#     date_meal date,
#     product_name text COLLATE pg_catalog."default",
#     weight real,
#     CONSTRAINT meal_pkey PRIMARY KEY (id),
#     CONSTRAINT fk FOREIGN KEY (user_id)
#         REFERENCES public.accounts (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION
# )

# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('говядина', 289, 20, 50, 60);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('свинина', 356, 15, 50, 60);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('баранина', 456, 25, 15, 50);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('курица', 210, 50, 45, 39);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('индейка', 452, 41, 10, 40);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('утка', 521, 15, 25, 37);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('капуста', 150, 5, 13, 2);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('огурцы', 42, 4, 2, 4);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('картошка', 123, 2, 35, 4);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('яблоко', 189, 3, 5, 2);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('апельсин', 115, 7, 25, 1);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('банан', 300, 8, 84, 6);
# INSERT INTO products(name, calories, proteins, carbon, fat) VALUES ('спагетти', 352, 12, 84, 40);


# SELECT calories, proteins FROM products INNER JOIN meal ON products.name = meal.product_name;

# SELECT calories, proteins FROM products, meal WHERE products.name = 'апельсин' AND meal.product_name = 'апельсин';