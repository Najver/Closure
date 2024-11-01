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

def append_jecna_postfix(username):
    """
    spoji string s @spsejecna.cz
    :param username:
    :return:
    """
    is_it_string(username)
    appended_string = username + "@spsejecna.cz"
    return appended_string

def append_seznam_postfix(username):
    """
        spoji string s @seznam.cz
        :param username:
        :return:
        """
    is_it_string(username)
    appended_string = username + "@seznam.cz"
    return appended_string


appender_postfix = append_jecna_postfix
#appender_postfix = append_seznam_postfix
print(appender_postfix("novak"))
a = 12
b = "Pepa"
print(append_jecna_postfix(b))
print(append_seznam_postfix(b))
