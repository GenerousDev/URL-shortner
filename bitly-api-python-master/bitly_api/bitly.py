import bitly_api

BITLY_ACCESS_TOKEN = '3a3db51ada5851cada371d283b341c8773aea3aa'
access =  bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)

full_link = input()

short_URL = access.shorten(full_link) 
print('Short_URL =',short_URL)