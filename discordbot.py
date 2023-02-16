import discord
from discord.ext import commands, tasks
import requests
import pygame
import button

intents = discord.Intents.default()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
token = "MTA2NDg0MjczMzk0NjE1MDkxMg.G9p2cr.o2nqoTr_u_AugOwSPD-Qcg5vQg_srprsFjqk24"


@bot.event
async def on_ready():
  print("Bot online!")
  await bot.change_presence(status=discord.Status.online)
  await bot.change_presence(activity=discord.Game(name="discord.py"))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def yt(ctx, *, message = None):
    """
    Searches youtube for the given keyword
    !yt <keyword>
    """
    if message == None:
        await ctx.send("Please enter something to be searched for")
    else:
        count = 1
        await ctx.send("How many video results do you want? Enter a number")
        x = await bot.wait_for('message', timeout = 6000)
        b = 0
        try:
            count = int(x.content)
        except:
            await ctx.send("You idiot. I specifically asked you for a NUMBER are you fucking stupid")
            b = 1
        req = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={message}&type=video&key=AIzaSyDpxLwFxhiKNVRbRgID808zGSOv9JnXMmw")
        if b == 0:
            if req.json()['pageInfo']['totalResults'] == 0:
                await ctx.send("No results found")
            else:
                url = "https://www.youtube.com/watch?v="
                for i in range(count):
                    final = url+req.json()['items'][i]['id']['videoId']
                    await ctx.send(final)

'''@bot.command()
async def urban(ctx, *, message = None):
    """
    Searches Urban Dictionary for the given phrase
    !urban phrase
    """
    if message == None:
        await ctx.send("Please enter a term to be searched")
    else:
        req = requests.get(f"https://api.urbandictionary.com/v0/define?term={message}")
        req = req.json()['list']
        a = len(req)
        if not len(req) <= 5:
            a = 5
        for i in range(a):
            embed = discord.Embed(
                title = message, description = "Here's some definitions"
            )
            definition = req[i]['definition']
            example = req[i]['example']
            embed.add_field(name="Definition",value=definition)
            embed.add_field(name="Example",value=example)
            await ctx.send(embed=embed)
            '''
@bot.command()
async def meme(ctx, message = ""):
    """
    Searches Reddit for a picture/meme
    !meme <optional_subreddit_name_goes_here>
    """
    req = requests.get("https://meme-api.com/gimme/"+message)
    try:
        await ctx.send(req.json()['preview'][-1])
    except:
        await ctx.send("Error, meme not found")

@bot.command()
async def define(ctx,message=None ):
    """
    Returns the definitions of a given word
    !define word
    """
    if message == None:
        await ctx.send("Please enter a word to be defined.")
    else:
        check_word_validity = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+message)
        if len(check_word_validity.json()) == 3:
            await ctx.send("Word not valid, try again.")
        else:
            definition_stuff = check_word_validity.json()[0]
            await ctx.send(f"Word: {definition_stuff['word']}")
            i = 0
            count = 0
            while True:
                try:
                    await ctx.send(f"Meaning: {definition_stuff['meanings'][i]['definitions'][0]['definition']}")
                    i += 1
                except:
                    break
            
@bot.command()
async def chuck(ctx):
    """
    Returns a random chuck norris joke
    """
    joke = requests.get("https://api.chucknorris.io/jokes/random").json()['value']
    await ctx.send(joke)

@bot.command()
async def get(ctx):
  """
  To get a list of your highlights
  """
  lines = []
  with open("todo.txt","r") as file:
    lines = file.readlines()
  for i in lines:
    await ctx.send(i)

@bot.command()
async def add(ctx, *, message = None):
  """
  Adds an item to the global highlights
  """
  if message == None:
    await ctx.send("Please enter something valid")
  b = 0
  with open("todo.txt","a") as file:
    if message != None:
      file.write(message)
      file.write("\n")
      b = 1
  if b == 1:
    await ctx.send("Message added")
      
@bot.command()
async def startreminder(ctx, *, message = "default reminder."):
    await ctx.send("Starting reminder...")
    if not studyshit.is_running():
        studyshit.start(message)

@bot.command()
async def stopreminder(ctx):
    await ctx.send("Stopping reminder...")
    studyshit.cancel()
@tasks.loop(hours = 1)
async def studyshit(message):
    await bot.wait_until_ready()
    channel = bot.get_channel(1056278732777717810)
    await channel.send(message)

@bot.command()
async def shutdown(ctx):
    ctx.send("Bye!")
    exit()




def discordbot():
    print(1)
    bot.run(token)


#youtube api key
#AIzaSyDpxLwFxhiKNVRbRgID808zGSOv9JnXMmw