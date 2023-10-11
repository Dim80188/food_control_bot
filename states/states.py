from aiogram.filters.state import StatesGroup, State

class Input_products(StatesGroup):
    change_input_products = State()
    change_product_categories = State()
    change_weight = State()

class Select_date(StatesGroup):
    start_period = State()
    end_period = State()

class Delete_data(StatesGroup):
    change_date = State()
    change_data = State()