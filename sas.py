import vk_api
import time
import random
import requests
vk = vk_api.VkApi(token="be1960c0de632c8a113bae5014c3b1537dc45cce13bbbb4915d08547cdf063a4cb77faf1a0c4772cd93c1")
while True:
    messages = vk.method("messages.getConversations", {"offset":0, "count":20, "filter":"unread"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() == "привет":
            vk.method("messages.send",{"peer_id": id,"message":"Ку! Как жизнь?","random_id": random.randint(0,999999990)}) 
            while True:
                messages = vk.method("messages.getConversations", {"offset":0, "count":20, "filter":"unread"})
                if messages["count"] >= 1:
                    id = messages["items"][0]["last_message"]["from_id"]
                    body = messages["items"][0]["last_message"]["text"]
                    if body.lower() == "норм":
                        vk.method("messages.send",{"peer_id": id,"message":"Это хорошо, я рад за тебя)","random_id": random.randint(0,999999992)})
                        break
                    else:
                        vk.method("messages.send",{"peer_id": id,"message":"Мяу, я тебя не понимаю(","random_id": random.randint(0,999999992)})
                        break
                    time.sleep(1)
        else:
            vk.method("messages.send",{"peer_id": id,"message":"Шо ти от мени хочешь Вася?","random_id": random.randint(0,999999998)})
    time.sleep(100000)
