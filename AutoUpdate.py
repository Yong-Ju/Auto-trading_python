from pywinauto import application, timings
import os, time
from private_folder import privatekey

# 실전투자 여부
REAL_TRADING = True

app = application.Application()
app.start('C:/KiwoomFlash3/bin/nkministarter.exe')

title = "번개3 Login"
dlg = timings.wait_until_passes(20, 0.5, lambda: app.connect(title=title).Dialog)

id_ctrl = dlg.Edit0
id_ctrl.set_focus()
id_ctrl.type_keys(privatekey.id)

pass_ctrl = dlg.Edit2
pass_ctrl.set_focus()
pass_ctrl.type_keys(privatekey.pw)

if REAL_TRADING:
    # 공인인증서 암호 저장창
    cert_ctrl = dlg.Edit3
    cert_ctrl.set_focus()
    cert_ctrl.type_keys(privatekey.pw2)

    btn_ctrl = dlg.Button0
    btn_ctrl.click()
else:
    btn_ctrl = dlg.Button0
    btn_ctrl.click()

    time.sleep(1)

    dlg2 = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title='번개3'))
    btn_ctrl2 = dlg2.Button1
    btn_ctrl2.click()

time.sleep(20)
os.system("taskkill /im nkmini.exe /f")

