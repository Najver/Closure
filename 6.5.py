def create_tourist_counter():
    amount_of_tourists = 0
    def add_tourist():
        nonlocal amount_of_tourists
        amount_of_tourists += 1
        return amount_of_tourists
    return add_tourist

add_new_tourist = create_tourist_counter()
amount = add_new_tourist()
print(amount)
amount = add_new_tourist()
print(amount)
amount = add_new_tourist()
print(amount)