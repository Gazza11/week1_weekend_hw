# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] = pet_shop['admin']['total_cash'] + amount
    return

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, pets_added):
    pet_shop['admin']['pets_sold'] = pet_shop['admin']['pets_sold'] + pets_added
    return pet_shop['admin']['pets_sold']

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, breed_input):
    amount = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed_input:
            amount.append(breed_input)
        
    return amount

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pet_shop['pets'].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    return pet_shop['pets'].append(new_pet)

def get_customer_cash(customer):
    return customer['cash']

