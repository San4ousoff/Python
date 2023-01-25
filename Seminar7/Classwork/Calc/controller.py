from calculation import calc
from user_interface import get_data as gd
import logger

def control_data():
    logger.log_all('Записываем переменные. Вызываем функции.')
    first_value, second_value, operator = gd()
    result = calc(first_value, second_value, operator)
    return result