import vk, random, time


vk_api_access_token = '9190d1ea76994bcbdaaa2f0980a67f1acbea8848aae4845033eb02969b772d6a427ca30aec628e7bd140e' 
album_id = 273529011



vk_api_version = '5.120'

session = vk.AuthSession(access_token = vk_api_access_token)
api = vk.API(session, v = vk_api_version)

user_info = api.users.get()
owner_id = user_info[0]['id']

offset = 0
photos_list = []
while True:
    photos_info = api.photos.get(owner_id = owner_id, album_id = album_id, offset = offset, count = 1000)['items']
    if photos_info != []:
        for photo in photos_info:
            photos_list.append(photo)
        offset += 1000
    else:
        break
        
photos_list_len = len(photos_list)
peer_id = (input('Введите айди диалога: '))

if peer_id[0] == 'c':
    list_peer_id = list(peer_id)
    list_peer_id.remove(list_peer_id[0])
    peer_id = ''
    for num in list_peer_id:
        peer_id += num
    peer_id = int(peer_id)
    peer_id = peer_id + 2000000000


while True:

    random_index = random.randint(0, photos_list_len - 1)
    media_id = photos_list[random_index]['id']

    
    api.messages.send(peer_id = peer_id, attachment = 'photo' + str(owner_id) + '_' + str(media_id), random_id = random.randint(-2147483648, 2147483647))

    print('Отправил пекчу https://vk.com/photo' + str(owner_id) + '_' + str(media_id) + '       [' + time.ctime() + ']\n')
    # режим спама с антиканчей
    time.sleep(15)
    # ручной режим
    # input()