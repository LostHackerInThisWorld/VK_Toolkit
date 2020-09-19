import vk_api, time, random, os

os.system("cls")

banner = """
____________________________________________________________________________
[1] - Спам в личные сообщения [2] - Спам комментариями под определенный пост
[3] - Очистить
____________________________________________________________________________
"""

print(banner)
while True:
	number = input("[Выберите 1,2,3]-> ")
	if number == "1":
		token_katemobile = input("Для спама в личные сообщения введите токен VK Admin: ") # Массив с токеном VK Admin
		usr_id = input("Цифровой(вечный) айди жертвы: ") # Massive
		msg_1 = input("Сообщение: ") # Massive
		while True:
			try:
				sessions = vk_api.VkApi(token = token_katemobile)
				vks = sessions.get_api()
				print("Сообщение - > ", msg_1, " -> ID: ",
				 vks.messages.send(user_id = usr_id, message = msg_1, random_id = random.randint(0, 9999999999)))
				time.sleep(3)
			except:
				print("Вы ввели неверный токен/айди или вк запросил капчу!")
				pass
	elif number == "2":
		token_vkadmin = input("Введите токен VK Admin: ") # Массив с токеном VK ADMIN
		own_id = input("Цифровой(вечный) айди вашей страницы: ") # Massive
		pst_id = input("Айди поста(в ссылке последние цифры после _): ") # Massive
		msg_2 = input("Комментарий: ")
		while True:
			try:
				session = vk_api.VkApi(token = token_vkadmin)
				vk = session.get_api()
				print(vk.wall.createComment(owner_id = own_id, post_id = pst_id,
				 message = msg_2, guid = random.randint(0, 9999999999)))
				time.sleep(3)
			except:
				print("Вы ввели неверный токен/айди или вк запросил капчу!")
				pass
	elif number == "3":
		os.system("cls")
		print(banner)
	else:
		print("Код не актуален, обновите его!")
	