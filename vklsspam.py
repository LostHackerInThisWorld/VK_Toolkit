import vk_api
import time
import random

my_token = 'token VkKateMobile'
msg = input('Msg: ')

session = vk_api.VkApi(token = my_token)
vk = session.get_api()

while True:
	try:
		vk.messages.send(user_id = айди кому спамить без '', message = msg, random_id = random.randint(0, 9999999999))
	except:
		pass
	time.sleep(3)
