import vk


vk_api_access_token = '9190d1ea76994bcbdaaa2f0980a67f1acbea8848aae4845033eb02969b772d6a427ca30aec628e7bd140e' 
vk_api_version = '5.120'

session = vk.AuthSession(access_token = vk_api_access_token)
api = vk.API(session, v = vk_api_version)
msg = "Сервер упал, но снова живёт"
api.messages.send(peer_id = 282902478, random_id = 0, message = msg)

