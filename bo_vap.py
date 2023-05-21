import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content != 'Cardapio':
            await message.channel.send(f'{message.author.name} Trabalhamos apenas com dois pratos:{os.linesep}1 - Stroganoff de Flango{os.linesep}2 - Caldo de Flango')
        # Mensagem direta para user
        elif message.content == 'Pedido Pronto?':
            await message.authot.send('Pedido em preparo.')
    # Boa vindas 
    async def on_member_join(self,member):
        guild = member.guild 
        if guild.sistem_channel is not None:
            mensagem = f'{member.mention} Bem- vindo, digite "Cardapio" para realizar o seu pedido no {guild.name}'
            await guild.system_channel.send(mensagem)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('MTEwOTYxNDkxMjEyMjEyNjM0Ng.GBD7jY.lp1LjMag0lYCCSBX_tTAeAZqgz5lYKa-dSp0Kc')