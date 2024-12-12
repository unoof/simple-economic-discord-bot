import discord                                                              #go to discord developer portal to active bot
import random
import json
import os

from discord.ui import Button, View
from dotenv import load_dotenv                                              #token for .env file
from discord.ext import commands                                            #outline

os.chdir("C:\\Users\\bobby\\Documents\\idk\\CNM-bot-main")

load_dotenv()
token = os.getenv('TOKEN')


intents = discord.Intents.all()
intents.message_content = True

client  =  commands.Bot(command_prefix = 'c.', intents=intents, help_command= None)              #bot preflix

@client.event                                                               #if the bot ready or not
async def on_ready():
    print("Bot now ready")
    print("-------------")



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

@client.command(aliases=['bal'])                                                           #make and check my bank or other account
async def balance(ctx, mention: discord.Member = None):
    if mention != None:
        await open_account(mention)

        users = await get_bank_data()

        wallet_amt = users[str(mention.id)]["money"]
    
        em = discord.Embed(title = f"{mention}'s balance", color = discord.Color.red())
        em.add_field(name= "money", value = wallet_amt)
        await ctx.send(embed = em)
    else:
        await open_account(ctx.author)
        user = ctx.author

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["money"]
    
        em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.red())
        em.add_field(name= "money", value = wallet_amt)
        await ctx.send(embed = em)

@client.command()                                                           #work earn 500 - 1000
@commands.cooldown(1, 10*60, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randint(500, 1500)

    await ctx.send(f"You work hard and earn: {earnings} money")

    users[str(user.id)]["money"] += earnings
    with open("bank.json",'w') as f:
        json.dump(users,f)

@client.command()                                                           #beg earn 0 - 500
@commands.cooldown(1, 15, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    i = random.randint(1, 1000)

    if i == 1:
        earnings = random.randint(151, 500)

        await ctx.send(f"Rain of money and you receive: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 2 <= i <= 50:
        earnings = random.randint(101, 150)

        await ctx.send(f"A generous person give you: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 51 <= i <= 150:
        earnings = random.randint(51, 100)

        await ctx.send(f"Since you are praying all day so somebody give you: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 151 <= i <= 350:
        earnings = random.randint(31, 50)

        await ctx.send(f"Someone think you homeless and give you: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 351 <= i <= 800:
        earnings = random.randint(20, 30)

        await ctx.send(f"You suck but still somebody give you: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    else:
        await ctx.send(f"You are so suck that nobody want to give you a shit!")

@client.command()                                                           #search earn 0 - 500
@commands.cooldown(1, 15, commands.BucketType.user)
async def search(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    i = random.randint(1, 1000)

    if i == 1:
        earnings = random.randint(151, 500)

        await ctx.send(f"You found a golden nugget and sold for: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 2 <= i <= 50:
        earnings = random.randint(101, 150)

        await ctx.send(f"You found a wallet and nobody near here, so you earn: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 51 <= i <= 150:
        earnings = random.randint(51, 100)

        await ctx.send(f"You found some sliver and sell for: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 151 <= i <= 350:
        earnings = random.randint(31, 50)

        await ctx.send(f"You found some money that somebody threw away: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    elif 351 <= i <= 800:
        earnings = random.randint(20, 30)

        await ctx.send(f"You found some trash but still can make some money from those: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)
    else:
        await ctx.send(f"You search hard but still found nothing, haha skill issues !!")

@client.command()                                                           #rob earn/lose 0 - 500
@commands.cooldown(1,3*60, commands.BucketType.user)
async def rob(ctx, mention: discord.Member):
    if mention != ctx.author:
        await open_account(ctx.author)
        await open_account(mention)

        users = await get_bank_data()

        thief = ctx.author
        victim = mention


        i = random.randint(1, 1000)

        if i == 1:
            amount = random.randint(151, 500)

            bal_of_thief = await update_bank(thief)
            bal_of_victim = await update_bank(victim)

            index = random.randint(1,2)
            if index == 2:
                if amount > bal_of_victim:
                    await ctx.send(f"{ctx.author.name} successful rob all {mention} money")

                    users[str(victim.id)]["money"] -= bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} money")

                    users[str(victim.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
            else:
                if amount > bal_of_thief:
                    await ctx.send(f"{thief.name} got caught and pay all money to {victim}")

                    users[str(victim.id)]["money"] += bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] -= bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                else:
                    await ctx.send(f"{thief.name} got caught and pay {amount} money to {victim}")

                    users[str(thief.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(victim.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

        elif 2 <= i <= 50:
            amount = random.randint(101, 150)

            bal_of_thief = await update_bank(thief)
            bal_of_victim = await update_bank(victim)

            index = random.randint(1,2)
            if index == 2:
                if amount > bal_of_victim:
                    await ctx.send(f"{ctx.author.name} successful rob all {mention} money")

                    users[str(victim.id)]["money"] -= bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} money")

                    users[str(victim.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
            else:
                if amount > bal_of_thief:
                    await ctx.send(f"{thief.name} got caught and pay all money to {victim}")

                    users[str(victim.id)]["money"] += bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] -= bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                else:
                    await ctx.send(f"{thief.name} got caught and pay {amount} money to {victim}")

                    users[str(thief.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(victim.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

        elif 51 <= i <= 150:
            amount = random.randint(51, 100)

            bal_of_thief = await update_bank(thief)
            bal_of_victim = await update_bank(victim)

            index = random.randint(1,2)
            if index == 2:
                if amount > bal_of_victim:
                    await ctx.send(f"{ctx.author.name} successful rob all {mention} money")

                    users[str(victim.id)]["money"] -= bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} money")

                    users[str(victim.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
            else:
                if amount > bal_of_thief:
                    await ctx.send(f"{thief.name} got caught and pay all money to {victim}")

                    users[str(victim.id)]["money"] += bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] -= bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                else:
                    await ctx.send(f"{thief.name} got caught and pay {amount} money to {victim}")

                    users[str(thief.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(victim.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

        elif 151 <= i <= 350:
            amount = random.randint(31, 50)

            bal_of_thief = await update_bank(thief)
            bal_of_victim = await update_bank(victim)

            index = random.randint(1,2)
            if index == 2:
                if amount > bal_of_victim:
                    await ctx.send(f"{ctx.author.name} successful rob all {mention} money")

                    users[str(victim.id)]["money"] -= bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} money")

                    users[str(victim.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
            else:
                if amount > bal_of_thief:
                    await ctx.send(f"{thief.name} got caught and pay all money to {victim}")

                    users[str(victim.id)]["money"] += bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] -= bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                else:
                    await ctx.send(f"{thief.name} got caught and pay {amount} money to {victim}")

                    users[str(thief.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(victim.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

        else:
            amount = random.randint(21, 30)

            bal_of_thief = await update_bank(thief)
            bal_of_victim = await update_bank(victim)

            index = random.randint(1,2)
            if index == 2:
                if amount > bal_of_victim:
                    await ctx.send(f"{ctx.author.name} successful rob all {mention} money")

                    users[str(victim.id)]["money"] -= bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += bal_of_victim
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
                else:
                    await ctx.send(f"{ctx.author.name} successful rob {mention}: {amount} money")

                    users[str(victim.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
            else:
                if amount > bal_of_thief:
                    await ctx.send(f"{thief.name} got caught and pay all money to {victim}")

                    users[str(victim.id)]["money"] += bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(thief.id)]["money"] -= bal_of_thief
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                else:
                    await ctx.send(f"{thief.name} got caught and pay {amount} money to {victim}")

                    users[str(thief.id)]["money"] -= amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)

                    users[str(victim.id)]["money"] += amount
                    with open("bank.json",'w') as f:
                        json.dump(users,f)
    else:
        await ctx.send("You cant rob yourself !!")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def toss(ctx, bet: int = None):
    if bet != None:
        if bet <= 0:
            await ctx.send("Please enter a valid amount of money !!")
        else:
            await open_account(ctx.author)

            bal = await update_bank(ctx.author)
            
            if bet > bal:
                await ctx.send("You don't have enough money !!")
            else:
                users = await get_bank_data()

                user = ctx.author

                users[str(user.id)]["money"] -= bet
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                button1 = Button(label= "front", style= discord.ButtonStyle.primary)
                button2 = Button(label= "back", style= discord.ButtonStyle.primary)

                i = random.randint(1, 2)
                channel = client.get_channel(1252953581942865980)
                await channel.send(f"{ctx.author} toss {bet} money and the coin is: {i}")

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 1:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*2} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*2
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button1.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 2:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*2} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*2
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button2.callback = button_callback

                view = View()
                view.add_item(button1)
                view.add_item(button2)
                em = discord.Embed(title = f"Choose one for chance to x2 the money you bet:", color = discord.Color.red())
                await ctx.send(embed = em, view = view)
    else:
        await ctx.send("Please enter a amount of money !!")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def dice(ctx, bet: int = None):
    if bet != None:
        if bet <= 0:
            await ctx.send("Please enter a valid amount of money !!")
        else:
            await open_account(ctx.author)

            bal = await update_bank(ctx.author)
            
            if bet > bal:
                await ctx.send("You don't have enough money !!")
            else:
                users = await get_bank_data()

                user = ctx.author

                users[str(user.id)]["money"] -= bet
                with open("bank.json",'w') as f:
                    json.dump(users,f)
                button1 = Button(emoji= "<:dice_1:1244828989969661953>", style= discord.ButtonStyle.primary)
                button2 = Button(emoji= "<:dice_2:1244828991915954337>", style= discord.ButtonStyle.primary)
                button3 = Button(emoji= "<:dice_3:1244828994227146863>", style= discord.ButtonStyle.primary)
                button4 = Button(emoji= "<:dice_4:1244828996236218418>", style= discord.ButtonStyle.primary)
                button5 = Button(emoji= "<:dice_5:1244828998597611572>", style= discord.ButtonStyle.primary)
                button6 = Button(emoji= "<:dice_6:1244829000682176633>", style= discord.ButtonStyle.primary)
                button7 = Button(emoji= "<:dice_7:1244829002691248189>", style= discord.ButtonStyle.primary)
                button8 = Button(emoji= "<:dice_8:1244829005488717916>", style= discord.ButtonStyle.primary)
                button9 = Button(emoji= "<:dice_9:1244829007363444767>", style= discord.ButtonStyle.primary)

                i = random.randint(1, 9)
                channel = client.get_channel(1252953581942865980)
                await channel.send(f"{ctx.author} dice {bet} money and the dice is: {i}")

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 1:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button1.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 2:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button2.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 3:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button3.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 4:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button4.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 5:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button5.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 6:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button6.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 7:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button7.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 8:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button8.callback = button_callback

                async def button_callback(interaction):
                    if interaction.user == ctx.author:
                        if i == 9:
                            em = discord.Embed(title = f"Congratulation you guess right: you won {bet*9} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                            users[str(user.id)]["money"] += bet*9
                            with open("bank.json",'w') as f:
                                json.dump(users,f)
                        else:
                            em = discord.Embed(title = f"You are so unlucky: you lose {bet} money", color = discord.Color.red())
                            await interaction.response.edit_message(embed = em, view = None)
                    else:
                        await interaction.response.send_message("You can not click this button !!", ephemeral=True)
                button9.callback = button_callback

                view = View()
                view.add_item(button1)
                view.add_item(button2)
                view.add_item(button3)
                view.add_item(button4)
                view.add_item(button5)
                view.add_item(button6)
                view.add_item(button7)
                view.add_item(button8)
                view.add_item(button9)
                em = discord.Embed(title = f"Choose one for chance to x9 the money you bet:", color = discord.Color.red())
                await ctx.send(embed = em, view = view)
    else:
        await ctx.send("Please enter a amount of money !!")

@client.command(aliases=['donate'])
async def give(ctx,mention: discord.Member, amount :int = None):
    if mention != ctx.author:
        if amount != None:
            await open_account(mention)
            await open_account(ctx.author)

            bal = await update_bank(ctx.author)
            if amount > bal:
                await ctx.send("You dont have enough money to gift !!")
            elif amount <= 0:
                await ctx.send("Invalid amount of money  !!")
            else:
                gift = await get_bank_data()

                user = ctx.author

                await ctx.send(f"{ctx.author.name} give {mention}: {amount} money")

                gift[str(user.id)]["money"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(gift,f)

                gift[str(mention.id)]["money"] += amount
                with open("bank.json",'w') as f:
                    json.dump(gift,f)
        else:
            await ctx.send("Please enter the money you want to give !!")
    else:
        await ctx.send("You cant give yourself money !!")

@client.command()
@commands.has_role('╰◆ ⌜Head Mod ⌟')
async def add(ctx, mention: discord.Member, amount: int = None):
    if amount != None:
        if amount <= 0:
            await ctx.send("Invalid amount of money")
        else:
            await open_account(mention)

            users = await get_bank_data()
        
            users[str(mention.id)]["money"] += amount
            with open("bank.json",'w') as f:
                json.dump(users,f)
            
            await ctx.send(f"Add {amount} money to {mention}'s balance")
    else:
        await ctx.send("Please enter the money you want to add !!")

@client.command()
@commands.has_role('╰◆ ⌜Head Mod ⌟')
async def remove_money(ctx, mention: discord.Member, amount: int = None):
    if amount != None:
        if amount <= 0:
            await ctx.send("Invalid amount of money")
        else:
            await open_account(mention)

            bal = await update_bank(mention)
            if amount >= bal:
                users = await get_bank_data()
        
                users[str(mention.id)]["money"] -= bal
                with open("bank.json",'w') as f:
                    json.dump(users,f)

                await ctx.send(f"Successful remove all {mention}'s money")
            else:
                users = await get_bank_data()
        
                users[str(mention.id)]["money"] -= amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)
            
                await ctx.send(f"Successful {amount} in {mention}'s money")
    else:
        await ctx.send("Please enter the money you want to remove !!")

@client.hybrid_command()
async def lb(ctx):
    users = await get_bank_data()
    leader_board = {}
    total = []

    for user in users:
        name = int(user)
        amount = users[user]["money"]
        leader_board[amount] = name
        total.append(amount)

    total = sorted(total, reverse= True)

    em = discord.Embed(title= f"Top 10 people with most money:", color= discord.Color.red())

    i = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        member_name = member.name 
        em.add_field(name= f"{i}. {member_name}", value= f"{amt}", inline= False)    
        if i == 10:
            break
        else:
            i = i+1
    await ctx.send(embed = em)
    await client.tree.sync()

@client.hybrid_command(aliases=['get_help'])
async def help(ctx):
    button1 = Button(label= "Commands", style= discord.ButtonStyle.primary)
    button2 = Button(label= "Chances", style= discord.ButtonStyle.primary)
    button3 = Button(label= "Source", style= discord.ButtonStyle.primary, url= "https://github.com/unoof/nknl-bot")
    button_back1 = Button(label="❌", style= discord.ButtonStyle.primary)

    async def button_callback(interaction):
        if interaction.user == ctx.author:

            button_back2 = Button(label="go back", style= discord.ButtonStyle.primary)
            button2 = Button(label= "Main commands", style= discord.ButtonStyle.primary)
            button3 = Button(label= "Mod only", style= discord.ButtonStyle.primary)

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"All main command:", color = discord.Color.red())
                    em.add_field(name= "balance/bal", value="Leave blank to check your self or @user/user_id to get someone else balance", inline= False)
                    em.add_field(name= "lb", value="Check top 10 people with most money", inline= False)
                    em.add_field(name= "work", value="10 mins cooldown", inline= False)
                    em.add_field(name= "beg", value="15 secs cooldown", inline= False)
                    em.add_field(name= "search", value="15 secs cooldown", inline= False)
                    em.add_field(name= "rob", value="3 mins cooldown", inline= False)
                    em.add_field(name= "toss +  money you want to bet)", value="chance to x2 the bet", inline= False)
                    em.add_field(name= "dice +  money you want to bet)", value="Chance to x9 the bet", inline= False)
                    em.add_field(name= "give/gift/donate + @user/userid + (amount)", value= "to give somebody any amount of money", inline= False)

                    view = View()
                    view.add_item(button_back2)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button2.callback = button_callback

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"All mod only command:", color = discord.Color.red())
                    em.add_field(name= "msg + #channel + (message you want)", value= "To send message to a specific channel", inline= False)
                    em.add_field(name= "add + @user/userid + (amount of money)", value= "To add some money to other balance  (only high mod can use this)", inline= False)
                    em.add_field(name= "remove money + @user/userid + (number)", value= "To remove an amount of money  (only high mod can use this)")

                    view = View()
                    view.add_item(button_back2)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button3.callback = button_callback

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"All command type:", color = discord.Color.red())

                    view = View()
                    view.add_item(button_back1)
                    view.add_item(button1)
                    view.add_item(button2)
                    view.add_item(button3)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button_back2.callback = button_callback

            em = discord.Embed(title = f"All command type:", color = discord.Color.red())

            view = View()
            view.add_item(button_back1)
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            await interaction.response.edit_message(embed = em, view = view)
        else:
            await interaction.response.send_message("You can not click this button !!", ephemeral=True)
    button1.callback = button_callback

    async def button_callback(interaction):
        if interaction.user == ctx.author:
            button1 = Button(label= "Work", style= discord.ButtonStyle.primary)
            button2 = Button(label= "Beg / Search/ Rob", style= discord.ButtonStyle.primary)
            button_back = Button(label="go back", style= discord.ButtonStyle.primary)

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"Work chance:", color = discord.Color.red())
                    em.add_field(name= "Random", value="500 - 1500")
                    view = View()
                    view.add_item(button_back)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button1.callback = button_callback
            
            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    em = discord.Embed(title = f"Beg / search/ rob chance:", color = discord.Color.red())
                    em.add_field(name= "0 money", value="20%", inline= False)
                    em.add_field(name= "20 - 30 money", value="45%", inline= False)
                    em.add_field(name= "31 - 50 money", value="20%", inline= False)
                    em.add_field(name= "51 - 100 money", value="10%", inline= False)
                    em.add_field(name= "101 - 150 money", value="4,9%", inline= False)
                    em.add_field(name= "151 - 500 money", value="0,1%", inline= False)
                    view = View()
                    view.add_item(button_back)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button2.callback = button_callback

            async def button_callback(interaction):
                if interaction.user == ctx.author:
                    view = View()
                    view.add_item(button_back1)
                    view.add_item(button1)
                    view.add_item(button2)
                    view.add_item(button3)
                    em = discord.Embed(title = f"Check the chance of these commands:", color = discord.Color.red())
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button_back.callback = button_callback

            view = View()
            view.add_item(button_back1)
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            em = discord.Embed(title = f"Check the chance of these commands:", color = discord.Color.red())
            await interaction.response.edit_message(embed = em, view = view)
        else:
            await interaction.response.send_message("You can not click this button !!", ephemeral=True)
    button2.callback= button_callback

    async def button_callback(interaction):
        if interaction.user == ctx.author:
            view = View()
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            em = discord.Embed(title = f"Get your help:", color = discord.Color.red())
            em.add_field(name= "Preflix", value="c.")
            await interaction.response.edit_message(embed = em, view = view)
        else:
            await interaction.response.send_message("You can not click this button !!", ephemeral=True)
    button_back1.callback = button_callback

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    em = discord.Embed(title = f"Get your help:", color = discord.Color.red())
    em.add_field(name= "Preflix", value="c.")
    await ctx.send(embed = em, view = view)
    await client.tree.sync()

@client.event
async def on_command_error(ctx, err):
    if err.__class__ is commands.MissingRole:
        await ctx.send(f'You dont have permission for this command !!!')
        return
    elif err.__class__ is commands.CommandOnCooldown:
        cd: int = int(err.retry_after)
        await ctx.send(f'The command is on cooldown, time left: **{cd//86400}d {(cd//3600)%24}h {(cd//60)%60}m {cd % 60}s**.')
        return

if __name__ == "__main__":
    client.run(token)                                               #bottoken to use