import discord, json
from discord.ext import commands

from account_development import open_account, get_bank_data, update_bank


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, mention: discord.Member = None):
        if mention:
            await open_account(mention)
            users = await get_bank_data()
            wallet_amt = users[str(mention.id)]["money"]

            em = discord.Embed(title=f"{mention}'s balance", color=discord.Color.red())
            em.add_field(name="money", value=wallet_amt)
            await ctx.send(embed=em)
        else:
            await open_account(ctx.author)
            users = await get_bank_data()
            wallet_amt = users[str(ctx.author.id)]["money"]

            em = discord.Embed(title=f"{ctx.author.name}'s balance", color=discord.Color.red())
            em.add_field(name="money", value=wallet_amt)
            await ctx.send(embed=em)

    @commands.command(aliases=['donate'])
    async def give(self, ctx,mention: discord.Member, amount :int = None):
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

    @commands.hybrid_command()
    async def lb(self, ctx):
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
            member = self.bot.get_user(id_)
            member_name = member.name 
            em.add_field(name= f"{i}. {member_name}", value= f"{amt}", inline= False)    
            if i == 10:
                break
            else:
                i = i+1

        await ctx.send(embed = em)

async def setup(bot):
    await bot.add_cog(Economy(bot))