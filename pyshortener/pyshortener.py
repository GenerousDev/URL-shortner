from pyshorteners import Shortener

ACCESS_TOKEN = '3a3db51ada5851cada371d283b341c8773aea3aa'

long_url = input()

url_shortener = Shortener(api_key = ACCESS_TOKEN)
print('Short URL is ',url_shortener.bitly.short(long_url))