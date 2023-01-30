import openai

import nextcord,time,datetime
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from nextcord.ext import application_checks



bot = commands.Bot()
# Apply for an API key at https://beta.openai.com
openai.api_key = "Put ur api key here"





model_engine = "text-davinci-002"



@bot.slash_command(name ="ask", description="askme")  # this will apear on the slash command
@application_checks.has_permissions(send_messages=True) # you don't need to put this but i recommed
async def my_first_command(interaction: Interaction,ask: 
    str = SlashOption(
        name="askquestion",
        description="askquestion",
        required=True,
        
        )): # you can add more command like slash option!

        print(ask)


        completions = openai.Completion.create(
            engine=model_engine,
            prompt=ask,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        # print(message)




        embed=nextcord.Embed(title=f'Answer!! {message}' )  # this is the embed you can config
        embed.set_thumbnail(url="https://cliply.co/wp-content/uploads/2021/08/372108630_DISCORD_LOGO_BLACK_400.gif") # you can put gif or picture in here
     

        await interaction.send(embed=embed,  ephemeral=True ) # after you finish the embed you need to send message back !

        # ephemeral is the message that send and visible just only you but if you want it to visible to everyone you can set it to false or delete it

        ds = open("dbTrain.txt", "w")
        ds.write(f'Ask : {ask} , Answer : {message}')
        ds.close()










@bot.event
async def on_ready():
    print(f"loging in : {bot.user}") # this just print bot name
    time.sleep(1.0)
    print("login sucess")
    await bot.change_presence(activity=nextcord.Streaming(name="putyourstatus",url="https://www.twitch.tv/Rawi1005")) # this is the status of the bot



bot.run("Discord Token")

