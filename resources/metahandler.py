# script by Mikey1234

import xbmc, xbmcgui
import shutil

localtxt1 = xbmc.getLocalizedString(31071)
localtxt2 = xbmc.getLocalizedString(31073)
localtxt3 = xbmc.getLocalizedString(31074)
localtxt4 = xbmc.getLocalizedString(31076)

path = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.module.metahandler/meta_cache',''))

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1 , localtxt4 , "" , localtxt3):
        meta=os.path.join(path, 'video_cache.db')
        try:
            os.remove(meta)
            xbmc.executebuiltin("Notification("+localtxt2+",XBMCHub TEAM)")
        except:
            xbmc.executebuiltin("Notification(File doesn't exists,XBMCHub TEAM)")        mydisplay = MyClass()
del mydisplay