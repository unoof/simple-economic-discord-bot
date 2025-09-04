import discord                                                             #go to discord developer portal to active bot
import os

from discord.ui import Button, View
from discord.ext import commands                                            #outline
from dotenv import load_dotenv                                              #token for .env file


load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.message_content = True

client  =  commands.Bot(command_prefix = 'e.', intents=intents, help_command= None)              #bot preflix

cogs = ["cogs.economy",
        "cogs.gamble",
        "cogs.mod",
        "cogs.chat_bot"]




@client.event                                                               #if the bot ready or not
async def on_ready():
    print("Bot now ready")
    print("-------------")
    print("cogs loaded:")
    for i in cogs: 
        await client.load_extension(i)
        print(i)
    await client.tree.sync()


@client.hybrid_command(aliases=['get_help'])
async def help(ctx):
    button1 = Button(label= "Commands", style= discord.ButtonStyle.primary)
    button2 = Button(label= "Chances", style= discord.ButtonStyle.primary)
    button3 = Button(label= "Source", style= discord.ButtonStyle.primary, url= "https://github.com/unoof/simple-economic-discord-bot")
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
                    em.add_field(name= "rob + @user/userid", value="3 mins cooldown", inline= False)
                    em.add_field(name= "toss +  money you want to bet", value="chance to x2 the bet", inline= False)
                    em.add_field(name= "dice +  money you want to bet", value="Chance to x9 the bet", inline= False)
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
                    em.add_field(name= "add + @user/userid + (amount of money)", value= "To add some money to other balance  (only high mod can use this)", inline= False)
                    em.add_field(name= "remove_money + @user/userid + (number)", value= "To remove an amount of money  (only high mod can use this)")

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
                    view.add_item(button2)
                    view.add_item(button3)
                    await interaction.response.edit_message(embed = em, view = view)
                else:
                    await interaction.response.send_message("You can not click this button !!", ephemeral=True)
            button_back2.callback = button_callback

            em = discord.Embed(title = f"All command type:", color = discord.Color.red())

            view = View()
            view.add_item(button_back1)
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
    em.add_field(name= "Preflix", value="e.")
    await ctx.send(embed = em, view = view)


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