#time_status v.1
import vk, datetime, time


vk_api_access_token = '9190d1ea76994bcbdaaa2f0980a67f1acbea8848aae4845033eb02969b772d6a427ca30aec628e7bd140e' 
vk_api_version = '5.120'

session = vk.AuthSession(access_token = vk_api_access_token)
api = vk.API(session, v = vk_api_version)
while True:


    now = datetime.datetime.now()
    # minute = now.minute()
    # if minute < 10:
    #      minute = '0' + str(minute)

    timee = str(now.hour) + ":" + str(now.minute)
    now_time = now.hour
    
   
    if now_time <= 6:
        api.status.set(text = timee + " :|")
        print("Установил статус" + str(api.status.get(user_id = 282902478)))
    elif now_time <= 12:
        api.status.set(text = timee + " O:)")
        print("Установил статус" + str(api.status.get(user_id = 282902478)))
    elif now_time <= 18:
        api.status.set(text = timee + " B-)")
        print("Установил статус" + str(api.status.get(user_id = 282902478)))
    elif now_time <= 22:
        api.status.set(text = timee + " xD")
        print("Установил статус" + str(api.status.get(user_id = 282902478)))
    time.sleep(60)  



