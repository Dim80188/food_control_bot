from aiogram.filters.state import StatesGroup, State

class Input_products(StatesGroup):
    change_input_products = State()
    change_product_categories = State()
    change_weight = State()