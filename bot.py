import requests
import discord
import json

bot = discord.Client()

riot_api_url = 'https://na1.api.riotgames.com/lol/'
riot_matches = 'match/v5/maches/by-puuid/'


dan_data = {
    'daily_games' : 0,
    'wins': 0,
    'kills' : 0,
    'deaths': 0,
    'assists' : 0,
    'time_wasted': 0,
}

@bot.event
async def on_ready():
    print('Dlz tracker active')

async def update_stats():
    pass
with open('auth.json') as f:
    auth = json.load(f)
    print(auth['secret'])
    bot.run(auth['secret'])
    f.close()
    