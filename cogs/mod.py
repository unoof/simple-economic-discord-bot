import discord, json

from discord.ext import commands
from account_development import open_account, get_bank_data, update_bank


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('mod')
    async def add(self, ctx, mention: discord.Member = None, amount: int = None):
        if mention is None:
            await ctx.send("Please enter the user you want to add !!")
        elif amount != None:
            if amount <= 0:
                await ctx.send("Invalid amount of money")
            else:
                await open_account(mention)

                users = await get_bank_data()
            
                users[str(mention.id)]["money"] += amount
                with open("bank.json",'w') as f:
                    json.dump(users,f)
                
                await ctx.send(f"Successful add {amount} money to {mention}'s balance")
        else:
            await ctx.send("Please enter the money you want to add !!")

    @commands.command()
    @commands.has_role('mod')
    async def remove_money(self, ctx, mention: discord.Member = None, amount: int = None):
        if mention is None:
            await ctx.send("Please enter the user you want to remove !!")
        elif amount != None:
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
                
                    await ctx.send(f"Successful remove {amount} in {mention}'s money")
        else:
            await ctx.send("Please enter the money you want to remove !!")

async def setup(bot):
    await bot.add_cog(Mod(bot))