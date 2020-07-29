#server_monitor v.1
import vk
from pyspectator.processor import Cpu
from time import sleep
  
cpu = Cpu(monitoring_latency=1)
with cpu:
    for __ in range(4):
        print(cpu.temperature)
        sleep(1.1)
while True:
    api.messages.send(peer_id = 2000000243, message = cpu.temperature)
    time.sleep(15)
    

