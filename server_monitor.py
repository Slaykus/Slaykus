#server_monitor v.1
import vk
from pyspectator.processor import Cpu
from time import sleep

vk_api_access_token = '9190d1ea76994bcbdaaa2f0980a67f1acbea8848aae4845033eb02969b772d6a427ca30aec628e7bd140e' 
vk_api_version = '5.120'

session = vk.AuthSession(access_token = vk_api_access_token)
api = vk.API(session, v = vk_api_version)
  
cpu = Cpu(monitoring_latency=1)

with cpu:
    for __ in range(4):
        print("Температура процессора - " + str(cpu.temperature) + "Градусов")
        sleep(1)
while True:
    api.messages.send(random_id = 0, peer_id = 282902478, message = "Температура процессора - " + str(cpu.temperature) + "Градусов")
    time.sleep(15)
    
