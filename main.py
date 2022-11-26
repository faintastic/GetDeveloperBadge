import discord
import os
import webbrowser  
from colorama import Fore as col
from discord.ext import commands

system = os.system

def menu():
    print(f"{col.BLUE}Hello! We are going to help you get the active developer badge!")
    tkn = input(f"{col.RED}Please input your bot token: ")
    print("Thank you! Please wait while we try and initialize the bot!")
    bot = commands.Bot(command_prefix=".")

    @bot.event
    async def on_ready():
        system("cls")
        print(f"{col.CYAN}Oauth link will open shortly.")
        webbrowser.open(f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=156766824512&scope=bot%20applications.commands")
        print(f"{col.RED}Logged in as {bot.user.name} : {bot.user.id}")

    @bot.slash_command(description="Pong")
    async def ping(ctx):
        await ctx.respond("Pong")

    bot.run(tkn)

if __name__ == "__main__":
    menu()
