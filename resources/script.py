
import xbmc, xbmcgui
import shutil
import glob, os

localtxt1 = xbmc.getLocalizedString(31066)
localtxt2 = xbmc.getLocalizedString(31073)
localtxt3 = xbmc.getLocalizedString(31074)

database = xbmc.translatePath('special://home/userdata/Database/MyMusic*.db')
    
class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1, localtxt3):
        RemoveVideodb()
        self.close()
        dialog = xbmcgui.Dialog()
        dialog.ok("XBMCHub TEAM","", localtxt2)
    
def RemoveVideodb():
    try:
        filelist = glob.glob(database)
        for f in filelist:
            os.remove(f)
    except:
        print 'ERROR'

mydisplay = MyClass()
del mydisplay