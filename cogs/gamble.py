import discord
import random, json

from discord.ui import Button, View
from discord.ext import commands

from account_development import open_account, get_bank_data, update_bank


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()                                                           #work earn 500 - 1000
    @commands.cooldown(1, 10*60, commands.BucketType.user)
    async def work(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()

        user = ctx.author

        earnings = random.randint(500, 1500)

        await ctx.send(f"You work hard and earn: {earnings} money")

        users[str(user.id)]["money"] += earnings
        with open("bank.json",'w') as f:
            json.dump(users,f)

    @commands.command()                                                           #beg earn 0 - 500
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def beg(self, ctx):
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

    @commands.command()                                                           #search earn 0 - 500
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def search(self, ctx):
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

    @commands.command()                                                           #rob earn/lose 0 - 500
    @commands.cooldown(1,3*60, commands.BucketType.user)
    async def rob(self, ctx, mention: discord.Member = None):
        if mention is None:
            await ctx.send("Please enter the user you want to rob !!")
        elif mention != ctx.author:
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

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def toss(self, ctx, bet: int = None):
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

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def dice(self, ctx, bet: int = None):
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

async def setup(bot):
    await bot.add_cog(Gamble(bot))