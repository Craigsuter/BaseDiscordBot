import discord
import os
import server
from discord.ext import commands
#imports
import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
from dotenv import load_dotenv
load_dotenv()
import datetime
from time import strptime
import asyncio
import time


#sets up command prefix
intents = discord.Intents.default()
client = commands.Bot(command_prefix = '!', intents=intents)



#This is the OG URL for Dota 2 / CSGO / Valo
#Posts once bot has started up
startup = datetime.datetime.now()

print("Bot started up at: ", startup)




#Logs the discord bot on
@client.event
async def on_ready():
    print("We have logged in as {0.user}.format(client)")
    #Sets presence
    await client.change_presence(activity=discord.Game(name="Bot is up and running!"))

    


#Starts the bot up to check for messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
      return
    
    guild=message.guild
    
    
#All commands that are blocked to none admins are found in here
    global currenttime
    global currentH
    global currentM
    global currentd
    currenttime =  datetime.datetime.now()
    #day
    currentd = currenttime.strftime("%d")
    #hour [UK time - 1]
    currentH = currenttime.strftime("%H")
    #Minute
    currentM = currenttime.strftime("%M")
    #Month
    currentmonth = currenttime.strftime("%m")
    #year
    currentyear = currenttime.strftime("%y")
    #second
    currentsecond = currenttime.strftime("%S")
    
    

    currentH = int(currentH)
    currentM = int(currentM)
    author=message.author
 


    #Gets segments of every message - full message found in 'fullMEssage to avoid over use of Discord API'
    fullMessage = message.content
    #This is the full message data useful for if you add the translation code
    nexttrans= fullMessage
    #This splits the message received into words, starting from 0 -> the length each slot matching a value
    sectionsofmessage = fullMessage.rsplit(" ")
    #This is the 1st word in the message
    introtomessage = sectionsofmessage[0]
    #This pulls the first character to the bot used for scanning for the prefix on line ~110
    first_char = introtomessage[0]
    #This pulls the channelID that the message was sent in
    channelDataID = message.channel.id

    #Getting the 2nd part of a message
    try:
      secondPartOfMessage= sectionsofmessage[1]
    except:
      secondPartOfMessage = "none"
      
      
    #The message will be converted into lower case so that commands can come in any captial / lowercase format for convenience!
    messagetolower = introtomessage
    messagereceived = messagetolower.lower()
    mention = f'<@!{client.user.id}>'
    #Checks for a ping of the bot
    


    
    if (first_char=="!"):
        #Put commands here that are the same for non mods + mods
        

        #None mod commands
        if (author.guild_permissions.administrator == False):



            if (messagereceived =="!help"):
              await message.channel.send("This is your first command! And it sends this response!")


            return





        #All Administrator commands  
        else:
            if (messagereceived =="!help"):
              await message.channel.send("This is your first command for admins! And it sends this response!")
       




client.run(os.getenv('TOKEN'))
server.server()
