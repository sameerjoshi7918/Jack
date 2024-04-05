import pyautogui as pg
import time
import webbrowser

#whatsapp checking that whether it is open
def call_this():
    titles=pg.getAllTitles()
    for i in range(len(titles)):
        if 'Brave' in titles[i]:
                #print(titles[i])
                print('brave found')
                openit=titles[i]
                break
    try:
        print('entered try')
        pg.getWindowsWithTitle(openit)[0].minimize()
        pg.getWindowsWithTitle(openit)[0].maximize()
        time.sleep(1)
    except:
        print('error Brave is not opened')
        webbrowser.open('https://www.google.com/')
        time.sleep(1)
    a=openit
    print(a)

    def okay():
        title=pg.getActiveWindowTitle()
        a1=title
        print('active window : ',title)
        def cc():
            time.sleep(1)
            if 'WhatsApp' in title:
                print('found')
            else:
                pg.hotkey('ctrl','tab')
                titl=pg.getActiveWindowTitle()
                if a1==titl:
                    webbrowser.open('https://web.whatsapp.com/')
                else:
                    cc()
        cc()
        
                
            
    okay()
#call_this()
