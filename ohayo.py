#ohayo
import vk, time, datetime, random
vk_api_access_token = '9190d1ea76994bcbdaaa2f0980a67f1acbea8848aae4845033eb02969b772d6a427ca30aec628e7bd140e' 

vk_api_version = '5.120'
love = ['заяк', 'любимая', 'родная', 'заяка', 'груша']
session = vk.AuthSession(access_token = vk_api_access_token)


now = datetime.datetime.now()

timee = str(now.hour) + ":" + str(now.minute)
now_time = now.hour

api = vk.API(session, v = vk_api_version)
love_r = random.choice(love)
while True:
    now = datetime.datetime.now()
    if now_time == 8:
        api.messages.send(user_id = 439068638, random_id = 0, message = "Доброе утро " + love_r)
        time.sleep(86400)
 

    
    
   
    
