import vk_api
import time
import random
import requests
from datetime import datetime
from selenium import webdriver

vk = vk_api.VkApi(
    token="be1960c0de632c8a113bae5014c3b1537dc45cce13bbbb4915d08547cdf063a4cb77faf1a0c4772cd93c1")

day = datetime.now().day


driver = webdriver.Chrome()

site = False

while site == False:
    try:
        driver.get("http://oreluniver.ru/schedule")
        site = True
    except:
        time.sleep(30)
        continue


btn = driver.find_elements_by_xpath(
    "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[2]/div/button[17]")
if len(btn) == 0:
    while len(btn) == 0:
        btn = driver.find_elements_by_xpath(
            "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[2]/div/button[17]")
        if len(btn) == 0:
            time.sleep(0.2)
        else:
            btn[0].click()
else:
    btn[0].click()


btn = driver.find_elements_by_xpath(
    "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div[2]/div/button[2]")
while len(btn) == 0:
    btn = driver.find_elements_by_xpath(
        "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div[2]/div/button[2]")
    time.sleep(0.2)
btn[0].click()



btn = driver.find_elements_by_xpath(
    "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/div/button[3]")
while len(btn) == 0:
    btn = driver.find_elements_by_xpath(
        "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/div/button[3]")
    time.sleep(0.2)
btn[0].click()

time.sleep(5)
res = ""
for j in range(6):
    if j == 0:
        res += "Пн:\n"
    elif j == 1:
        res += "Вт:\n"
    elif j == 2:
        res += "Ср:\n"
    elif j == 3:
        res += "Чт:\n"
    elif j == 4:
        res += "Пт:\n"
    elif j == 5:
        res += "Сб:\n"

    for i in range(8):
        try:
            title = driver.find_element_by_xpath(
                "/html/body/div[4]/div/div/div[2]/div/div[3]/table/tbody/tr[" + str(i + 1) + "]/td[" + str(j + 2) + "]/h5")
            if i == 0:
                res += title.text + "(8:30-10:00)" + "\n"
            elif i == 1:
                res += title.text + "(10:10-11:40)" + "\n"
            elif i == 2:
                res += title.text + "(12:00-13:30)" + "\n"
            elif i == 3:
                res += title.text + "(13:40-15:10)" + "\n"
            elif i == 4:
                res += title.text + "(15:20-16:50)" + "\n"
            elif i == 5:
                res += title.text + "(17:00-18:30)" + "\n"
            elif i == 6:
                res += title.text + "(18:40-20:10)" + "\n"
            elif i == 7:
                res += title.text + "(20:20-21:50)" + "\n"
        except:
            pass
    res += "\n\n"
driver.quit()

while True:
    messages = vk.method("messages.getConversations", {
                         "offset": 0, "count": 20,
                         "filter": "unread"})
    if messages["count"] >= 1:

        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]

        if body.lower() == "расписание":
            
            vk.method("messages.send", {
                      "peer_id": id, "message": res, "random_id": random.randint(0, 999999990)})
        else:
            vk.method("messages.send", {
                      "peer_id": id,
                      "message": "Привет, я бот Алексея из 81ПМ, пока могу подсказать только расписание для второго курса, напиши 'Расписание'",
                      "random_id": random.randint(0, 999999998)})
    time.sleep(1)
    if day == datetime.now().day:
        pass
    else:
        day = datetime.now().day


        driver = webdriver.Chrome()
        driver.get("http://oreluniver.ru/schedule")
        time.sleep(3)

        btn = driver.find_elements_by_xpath(
            "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[2]/div/button[17]")
        btn[0].click()

        time.sleep(3)
        btn = driver.find_elements_by_xpath(
            "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div[2]/div/button[2]")
        btn[0].click()

        time.sleep(3)
        btn = driver.find_elements_by_xpath(
            "/html/body/div[4]/div/div/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/div/button[3]")
        btn[0].click()

        time.sleep(5)
        res = ""
        for j in range(6):
            if j == 0:
                res += "Пн:\n"
            elif j == 1:
                res += "Вт:\n"
            elif j == 2:
                res += "Ср:\n"
            elif j == 3:
                res += "Чт:\n"
            elif j == 4:
                res += "Пт:\n"
            elif j == 5:
                res += "Сб:\n"

            for i in range(8):
                try:
                    title = driver.find_element_by_xpath(
                        "/html/body/div[4]/div/div/div[2]/div/div[3]/table/tbody/tr[" + str(i + 1) + "]/td[" + str(j + 2) + "]/h5")
                    if i == 0:
                        res += title.text + "(8:30-10:00)" + "\n"
                    elif i == 1:
                        res += title.text + "(10:10-11:40)" + "\n"
                    elif i == 2:
                        res += title.text + "(12:00-13:30)" + "\n"
                    elif i == 3:
                        res += title.text + "(13:40-15:10)" + "\n"
                    elif i == 4:
                        res += title.text + "(15:20-16:50)" + "\n"
                    elif i == 5:
                        res += title.text + "(17:00-18:30)" + "\n"
                    elif i == 6:
                        res += title.text + "(18:40-20:10)" + "\n"
                    elif i == 7:
                        res += title.text + "(20:20-21:50)" + "\n"
                except:
                    pass
            res += "\n\n"
        driver.quit()
