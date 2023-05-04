import discord

TOKEN = 'your_bot_token_here'
COPY_COMMAND = '!copy'
COPY_FROM_CHANNEL_ID = 123456789012345678 # Replace with the actual ID of the channel to copy from
COPY_TO_CHANNEL_ID = 123456789012345678 # Replace with the actual ID of the channel to copy to

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(COPY_COMMAND):
        channel = client.get_channel(COPY_FROM_CHANNEL_ID)
        async for msg in reversed(channel.history(limit=-1)):
            if msg.content != COPY_COMMAND:
                await client.get_channel(COPY_TO_CHANNEL_ID).send(msg.content)

client.run(TOKEN)
