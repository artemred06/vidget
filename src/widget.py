from masks import get_mask_card_number, get_mask_account

def mask_account_card(information: str) -> str:
    """Функция маскировки номера карты или банковского счета"""

    #Разделение строки информации полученной из аргумента
    parts = information.strip().split()
    name = " ".join(parts[:-1])
    number = parts[-1]

    #При условии, что пользователь ввел мало данных, возвращаем изначальную строку
    if len(parts) < 2:
        return information

    #Маскировка номера в зависимости от названия продукта
    if name == "Счет":
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)

    mask = name + " " + mask_number

    return mask


def get_date(input_date: str) -> str:
    """Функция определения даты из входящей строки"""

    #Создание списка из дня, месяца и года
    list_date = input_date[:10].split(sep="-")

    #Распределение по именуемым переменным
    day = list_date[2]
    month = list_date[1]
    year = list_date[0]

    date = f"{day}.{month}.{year}"

    return date

