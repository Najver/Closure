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

def append_jecna_postfix(username:str):
    """
    spoji string s @spsejecna.cz
    :param username:
    :return:
    """
    is_it_string(username)
    appended_string = username + "@spsejecna.cz"
    return appended_string

def append_seznam_postfix(username:str):
    """
        spoji string s @seznam.cz
        :param username:
        :return:
        """
    is_it_string(username)
    appended_string = username + "@seznam.cz"
    return appended_string

def create_email(appender_function, username):
    """
    vytvari koncovu mejlu podle parametru appender_function
    :param appender_function:
    :param username:
    :return:
    """
    return appender_function(username)

appender_postfix = append_jecna_postfix
print(create_email(appender_postfix, "novak"))
appender_postfix = append_seznam_postfix
print(create_email(appender_postfix, "novak"))