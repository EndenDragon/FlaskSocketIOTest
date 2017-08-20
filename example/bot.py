import discord
import socketio

client = discord.Client()
external_sio = socketio.AsyncRedisManager('redis://', write_only=True, channel='flask-socketio')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    await external_sio.emit('on_message', data={'content': message.content}, namespace='/test')
    print("emitted")

client.run('MzQ4NzE2OTczMDcwNDgzNDU3.DHq_fw.yNzvp4Fb9izkxORBLz40kQ8aAFU')