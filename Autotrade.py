from pywinauto import application
from pywinauto import timings
import time
import os
from private import privatekey

print(privatekey.id)
print(privatekey.pw)

#
# app = application.Application()
# app.start("C:/KiwoomHero4/Bin/nkstarter.exe")
#
# title = "영웅문4 Login"
# # dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))
# dlg = timings.wait_until_passes(20, 0.5, lambda: app.window(title=title))


# pass_ctrl = dlg.Edit2
# pass_ctrl.set_focus()
# pass_ctrl.type_keys('private')
#
# cert_ctrl = dlg.Edit3
# cert_ctrl.set_focus()
# cert_ctrl.type_keys('lspwd')
#
# btn_ctrl = dlg.Button0
# btn_ctrl.click()
