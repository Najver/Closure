from tkinter.tix import INTEGER


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

def is_it_int(data):
    if type(data) is int:
        return True
    else:
        raise Exception("You need to enter a integer")


def formatuj_prijimeni_prvni(jmeno:str,prijmeni:str):
    """
    fromatuje jmeno na prijmeni pak jmeno
    :param jmeno:
    :param prijmeni:
    :return:
    """
    is_it_string(jmeno)
    is_it_string(prijmeni)
    formated = prijmeni + " " + jmeno
    return formated
def formatuj_monogram(jmeno:str,prijmeni:str):
    """
    formatuje na prvni pismeno ve jmeno.prvni pismeno v prijemni
    :param jmeno:
    :param prijmeni:
    :return:
    """
    is_it_string(jmeno)
    is_it_string(prijmeni)
    formated = f"{prijmeni[0]}.{jmeno[0]}."
    return formated

def vyber_formatovaci_funkci(delka):
    """
    vybira jakou funkci pouzije podle delky
    :param delka:
    :return:
    """
    is_it_int(delka)
    if delka < 4 and delka > 0:
        return formatuj_monogram
    elif delka > 4:
        return formatuj_prijimeni_prvni
    else:
        raise Exception("You need to enter a positive number")


print(formatuj_prijimeni_prvni("Jan", "Poloch"))
print(formatuj_monogram("Jan", "Poloch"))

formatovac = vyber_formatovaci_funkci(3)
print(formatovac("Jan", "Novak"))
formatovac = vyber_formatovaci_funkci(155)
print(formatovac("Jan", "Novak"))