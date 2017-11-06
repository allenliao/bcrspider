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
    wait("loginBtn.png", 10)
    
    if screenRegion.find("account_cache.png"):
        screenRegion.find("loginBtn.png").click()
    else:
        screenRegion.find("account.png").click()
        type(username)
        screenRegion.find("password.png").click()
        type(password)
        screenRegion.find("loginBtn.png").click()
    
    screenRegion.find("loginConfirmBtn.png").click()
    screenRegion.find("LDRBtn.png").click()#真人娛樂
    screenRegion.find("SAGameBtn.png").click()#沙龍魚樂
    wait("multiGameBtn.png", FOREVER)
    screenRegion.find("multiGameBtn.png").click()#多人頭注
    
    #TODO:抽到設定檔
    tableRegion1=Region(255,125,410,865)
    tableRegion2=Region(705,125,410,865)
    tableRegion3=Region(1153,125,410,865)
    
    initTable(tableRegion1,"BCR01Btn.png")
    tableRegion2.find("selectTable.png").click()#select Table
    initTable(tableRegion2,"BCR02Btn.png")
    tableRegion3.find("selectTable.png").click()#select Table
    initTable(tableRegion3,"BCR03Btn.png")
    
    
    
    
def initTable(tableRegion,BCRBtnImg):
    wait(BCRBtnImg, 8)
    tableRegion.find(BCRBtnImg).click()#Table1
    wait("closeVideo.png", 5)
    tableRegion.find("closeVideo.png").click()#close Video
    getTableInfo(tableRegion)
    
def countDownStart(event):
    print(getName(event.region)+" start countdown")

def getTableInfo(tableRegion):
    #TODO:抽到設定檔
    print ("getTableInfo!! called")
    tableRegion.onAppear("countDownStart.png", countDownStart)#倒數
    tableRegion.observe(FOREVER ,background=True)

def getName(tableRegion):
    return {
        "tableRegion1": "Table 1"
    }.get(tableRegion, "Table 1")    # 9 is default if x not found

    

if __name__ == "__main__":
    screenRegion = Screen()
    readConfig()
    #getTableInfo()
    #load config
    #login
    
    #observeFunc(folder_tblRegion)
    #observeFunc(file_tblRegion)