def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    mask_card_number = card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:]
    return mask_card_number


def get_mask_account(account: int) -> str:
    """Функция маскировки номера банковского счета"""
    account = str(account)
    mask_account = "**" + account[-4:]
    return mask_account
