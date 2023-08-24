# The Request Library In Python
import requests

r = requests.get('https://pbs.twimg.com/media/F4PCGU4WsAAWlL2?format=webp&name=small')

# with open('rick.png', 'wb') as f:
#     f.write(r.content)

print(r.headers)
