import random
def is_it_string(string):
    """
    kontroluje jestli uzivatel vlozil string
    :param string:
    :return:
    """
    if type(string) is str:
        return True
    else:
        raise Exception("You need to enter a string")

def convert_to_upperlatters(text):
    """
    prevede text na velka pismena
    :param text:
    :return:
    """
    is_it_string(text)
    text = text.upper()
    return text


def convert_empty_to_smile(text):
    """
    prevede mezery v text na smajliky
    :param text:
    :return:
    """
    is_it_string(text)
    text = text.replace(" ", ":)")
    return text


def convert_v_to_w(text):
    """
    prevede v na w
    :param text:
    :return:
    """
    is_it_string(text)
    text = text.replace("V","W")
    text = text.replace("v","w")
    return text


def add_star_to_beggining_and_end(text):
    """
    prida * na zacatek a na konec
    :param text:
    :return:
    """
    is_it_string(text)
    text = f"*{text}*"
    return text


def convert_to_mulitiples(text):
    """
    prevede znaky ? a ! v textu na vice znaku
    :param text:
    :return:
    """
    is_it_string(text)
    text = text.replace("?", "???")
    text = text.replace("!", "!!!!!")
    return text


functions_list = [convert_to_upperlatters, convert_empty_to_smile, convert_v_to_w,add_star_to_beggining_and_end,convert_to_mulitiples]

def funky_format(text):
    """
    vybere nahodnu metodu v liste metod, opakuje se 3x
    :param text:
    :return:
    """
    rounds = 0
    while rounds < 3:
        choice = random.choice(functions_list)
        text = f"{choice(text)}"
        rounds += 1
    return text



print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))