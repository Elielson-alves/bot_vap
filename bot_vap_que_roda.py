import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")
class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        message.content = message.content.lower()

        if message.content == 'cardapio':
            await message.channel.send(f'{message.author.name}, trabalhamos apenas com dois pratos:\n1 - Stroganoff de Frango\n2 - Caldo de Frango')
        elif message.content == '1':
            await message.channel.send(f'{message.author.name}, Pedido do Stroganoff de Frango em preparo.')
        elif message.content == '2':
            await message.channel.send(f'{message.author.name}, Pedido do Caldo de Frango em preparo.')
        elif message.content == 'pedido pronto?':
            await message.channel.send(f'{message.author.name},Pedido em preparo, aguarde.')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} Bem-vindo, digite "Cardapio" para realizar o seu pedido no {guild.name}'
            await guild.system_channel.send(mensagem)

intents = discord.Intents.all()
intents.members = True

client = MyClient(intents=intents)
client.run(token)