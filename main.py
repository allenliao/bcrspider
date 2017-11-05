import json
from sikuli.Sikuli import *

def readConfig():
    buConfigFile = open('buconfig.json','r')
    #buconfigFile.read()
    buConfigStr=buConfigFile.read()
    #print buConfigStr
    
    buConfigObj=json.loads(buConfigStr)
    buurl=buConfigObj['buurl']
    username=buConfigObj['username']
    password=buConfigObj['password']
    print buurl
    openWebSiter(buurl)
    loginAndOpenGame(username,password)

def openWebSiter(buurl):
    openApp(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe "+buurl)
    
def loginAndOpenGame(username,password):
    if s.find("account_cache.png"):
        s.find("loginBtn.png").click()
    else:
        s.find("account.png").click()
        type(username)
        s.find("password.png").click()
        type(password)
        s.find("loginBtn.png").click()
    
    s.find("loginConfirmBtn.png").click()
    s.find("LDRBtn.png").click()#真人娛樂
    s.find("SAGameBtn.png").click()#沙龍魚樂
    wait("multiGameBtn.png", FOREVER)
    s.find("multiGameBtn.png").click()#多人頭注
    wait("BCR01Btn.png", 5)
    s.find("BCR01Btn.png").click()#Table1
    s.find("selectTable.png").click()#select Table
    s.find("BCR02Btn.png").click()#Table2
    s.find("selectTable.png").click()#select Table
    s.find("BCR03Btn.png").click()#Table3
    s.find("closeHint.png").click()#close hint

    

    

if __name__ == "__main__":
    s = Screen()
    readConfig()
    #load config
    #login
    
    #observeFunc(folder_tblRegion)
    #observeFunc(file_tblRegion)