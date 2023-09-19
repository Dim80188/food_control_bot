

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