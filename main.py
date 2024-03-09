import os
import discord
from dotenv import load_dotenv
from startserverundetected import startingServer, get_player_names
load_dotenv()
import os
import discord
import time
# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('SERVER_ID')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  for server in client.guilds:
    if server.name == SERVER:
      print(f'{client.user.name} has connected to {server.name}!')

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    try:
        general = client.get_channel(1102600792185262133)
        if message.content.startswith('!start'):
            await general.send('Starting server...')
            timeTaken = startingServer(True)
            if timeTaken:
                await general.send(f'Server started in {timeTaken} seconds')
            else:
                timeStarted = time.time()
                await general.send('Error: server already running')
        if message.content.startswith('!time'):
            serveroff = startingServer(False)
        if serveroff:
            await general.send('The server is currently off!')
        else:
            await general.send(f'The server has been on for {time.gmtime(timeStarted-time.time())}')
        if message.content.startswith('!status'):
            if startingServer(False) == False:
                await general.send('The server is currently on!')
        else:
            await general.send('The server is currently off!')
        if message.content.startswith('!online'):
            result = ", ".join([item for item in get_player_names()])
        if result:
            await general.send(f'{result} are currently online.')
        else:
            await general.send('No one is currently online.')
    except:
        general.send("An error occured processing your request. Please try again.")
        
        
        

client.run(TOKEN)