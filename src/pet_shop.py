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

def remove_customer_cash(customer, amount):
    customer ['cash'] = customer['cash'] - amount
    return customer['cash']

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, new_pet):
    return customer['pets'].append(new_pet)

#Optional

def customer_can_afford_pet(customer, new_pet):
    if customer['cash'] >= new_pet['price']:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, new_pet, customer):
    #If pet not found skip below
    if new_pet == None:
        return None
    elif customer['cash'] < new_pet['price']:
        return None
    else:
        add_pet_to_customer(customer, new_pet) #add pet to customer's list
        add_or_remove_cash(pet_shop, new_pet['price']) #add petshop cash
        remove_customer_cash(customer, new_pet['price']) #remove cash from customer
        remove_pet_by_name(pet_shop, new_pet) #Remove pet from list
        increase_pets_sold(pet_shop, 1) #Increase total sales
