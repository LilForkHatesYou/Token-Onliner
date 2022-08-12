import json, random, sys, re, threading, time, httpx, os, websocket, fade
from concurrent.futures import ThreadPoolExecutor
from colr import color
def online(token, game, type, status):
    ws = websocket.WebSocket()
    if status == "random":
        stat = ['online', 'dnd', 'idle']
        status = random.choice(stat)
    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    hello = json.loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    if type == "1":
        gamejson = {"name": game,"type": 0}
    elif type == '2':
        gamejson = {"name": game,"type": 1,"url": "https:/twitch.tv/LilFork"}
    elif type == "4":
        gamejson = {"name": game,"type": 2}
    elif type == "3":
        gamejson = {"name": game,"type": 3}
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": sys.platform,"$browser": "RTB","$device": f"{sys.platform} Device"},"presence": {"game": gamejson,"status": status,"since": 0,"afk": False}},"s": None,"t": None}
    ws.send(json.dumps(auth))
    ack = {"op": 1,"d": None}
    while True:
        time.sleep(heartbeat_interval / 1000)
        try:
            ws.send(json.dumps(ack))
        except Exception as e:
            break
def main():
    type = input(color(f'Options: [1] Playing | [2] Streaming | [3] Watching | [4] Listening\nYour Choice > ', fore='green', style='bright'))
    os.system("cls")
    game = input(color(f'Info: Type what you want the status to be\nStatus > ', fore='green', style='bright'))
    os.system('cls')
    status = ['online', 'dnd', 'idle','random']
    status = status[3]
    executor = ThreadPoolExecutor(max_workers=1000)
    while True:
        for token in open("tokens.txt","r+").readlines():
            threading.Thread(target=lambda : online(token.replace("\n",""), game, type, status)).start()
        fart = "[!] Tokens Online"
        poopcum = fade.random(fart)
        print(poopcum)
        time.sleep(60)
        os.system('cls')

main()