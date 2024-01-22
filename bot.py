import discord
from datetime import datetime
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True  # Enable this if you want to access message.content

client = discord.Client(intents=intents)
token = "MTE5MzAzNzA0OTc4NDE3MjYzNQ.GfRpLz.brIzFmiGQ-ckWu-Ozo3TQwMmclIg3P8DFp-Q98"  # Replace with your bot token
channel_id = 1193033938160078951

target_time = "18:00"  

@tasks.loop(seconds=60)  # Run the loop every 60 seconds
async def time_module():
    current_time = datetime.now().strftime("%H:%M")
    if current_time == target_time:
        print("time module ended")
        time_module.stop()  # Stop the loop

@client.event
async def on_ready():
    print("bot:user ready == {0.user}".format(client))
    channel = client.get_channel(channel_id)
    await channel.send("@everyone Did you escape the matrix today")

    # Start the time_module loop
    time_module.start()

client.run(token)