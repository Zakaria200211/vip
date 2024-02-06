#• DeCoDe By @H_S_W_M •
import webbrowser
import os
import threading
import random
import requests
from rich.panel import Panel as nel
from rich import print as cetak
from uuid import uuid4
uid = uuid4()
os.system('clear')
print('')
def banner():
	pass
print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
print()
token = input('- Kilwa • T O K E N  : ')
print('\n')
ID = input('- Kilwa • I D   : ')
tlk = '''
• DeCoDe By @H_S_W_M •
تـم تفعيل اداة متاحات التيك توك

لاتنسى صور الصيد 🔥

- Kilwa @Lx0b2 - @Pythonln
'''
requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(tlk))
webbrowser.open_new_tab('https://t.me/Pythonln')
print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
print('\n- Kilwa • .......جاري الانطلاق انتظر')
def sui():
  while True:
    try:
        user = '1234567890.asdfghjklqwertyuiopzxcvbnm'
        num = ('Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley', 'Jennifer', 'Joshua', 'Amanda', 'David', 'Daniel', 'James', 'Robert', 'John', 'Joseph', 'Andrew', 'Ryan', 'Brandon', 'Jason', 'Justin', 'Sarah', 'William', 'Jonathan', 'Stephanie', 'Brian', 'Nicole', 'Nicholas', 'Anthony', 'Heather', 'Elizabeth', 'Megan', 'Adam', 'Eric', 'Melissa', 'Kevin', 'Steven', 'Thomas')
        rang = str(''.join(random.choice(num) for i in range(1)))
        name = str(''.join(random.choice(user) for i in range(6)))
        import concurrent.futures
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=100)
        executor.submit(sui)
        username = name
        email = name + '@gmail.com'
        res = requests.get(f'''https://GmailandTiktokandzaid.zaidbot.repl.co/2/email={email}''').text
        if '"Dev":"@uiujq","Email":"Good"' in res:
            print(f'''OK GMAIL : {email}''')
        api = requests.get(f'''https://api.dlyar-dev.tk/info-tiktok.json?user={username}''').json()
        if api['status']:
            name = api['name']
            followers = api['followers']
            following = api['following']
            like = api['likes']
            id = api['id']
            code = api['code-country']
            country = api['country']
            tlg = f'''
• DeCoDe By @H_S_W_M •
<───━𓌹 𝑲𝑰𝑳𝑾𝑨 𓌺━───>
Name : {name}
Username : {username}
Email : {email}
<───━𓌹 𝑲𝑰𝑳𝑾𝑨 𓌺━───>
 By ~ @Lx0b2 ~ @Pythonln'''
            requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(tlg))
            tlkg = f'''
• DeCoDe By @H_S_W_M •
<───━𓌹 𝑲𝑰𝑳𝑾𝑨 𓌺━───>
Name : {name}
Username : {username}
Email : {email}
Id = id = tg://openmessage?user_id={ID}
<───━𓌹 𝑲𝑰𝑳𝑾𝑨 𓌺━───>
 By ~ @Lx0b2 ~ @Pythonln'''

            cetak(nel(tlg,style='green',title='ايميل متاح'))
        else:
            cetak(nel(f'''\x1b[1;31m BAD GMAİL - غير شغال • {email}'''))
    except:
        cetak(nel(f'''\x1b[1;31m BAD GMAİL - غير شغال • {email}'''))
Threads = []
for t in range(4):
    x = threading.Thread(target=sui)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
sui()