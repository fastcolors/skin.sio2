# script by Mikey1234

import xbmc, xbmcgui
import shutil

localtxt1 = xbmc.getLocalizedString(31080)
localtxt2 = xbmc.getLocalizedString(31073)

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("", localtxt1):
        path = xbmc.translatePath(os.path.join('special://home/userdata',''))
        advance=os.path.join(path, 'advancedsettings.xml')
        try:
            os.remove(advance)
            xbmc.executebuiltin("Notification("+localtxt2+",XBMCHub TEAM)")
        except:
            xbmc.executebuiltin("Notification(File doesn't exists,XBMCHub TEAM)")
        
      mydisplay = MyClass()
del mydisplay