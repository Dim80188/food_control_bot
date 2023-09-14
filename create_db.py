# CREATE TABLE accounts
# (
# 	id serial PRIMARY KEY,
# 	id_telegram bigint,
# 	user_name text
# );
# CREATE TABLE meal
# (
# 	id serial PRIMARY KEY,
# 	user_id bigint,
# 	date_meal date,
# 	product_name text,
# 	weight real
# )
# CREATE TABLE IF NOT EXISTS public.exercises
# (
#     user_id bigint,
#     date_train date,
#     name text COLLATE pg_catalog."default",
#     repetitions integer,
#     weight real
# )

# TABLESPACE pg_default;
#
# ALTER TABLE IF EXISTS public.exercises
#     OWNER to postgres;