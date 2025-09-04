import json


async def open_account(user):                                               #bank system
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["money"] = 0
    
    with open("bank.json",'w') as f:                                        #json file for database
        json.dump(users, f)
    return True

async def get_bank_data():
    with open("bank.json",'r') as f:
        users = json.load(f)
    return users

async def update_bank(user, change = 0, mode = "money"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", 'w') as f:
        json.dump(users,f)

    bal = users[str(user.id)]["money"]
    return bal
