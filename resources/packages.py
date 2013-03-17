# script by Mikey1234

import xbmc, xbmcgui
import shutil

localtxt1 = xbmc.getLocalizedString(31067)
localtxt2 = xbmc.getLocalizedString(31073)
localtxt3 = xbmc.getLocalizedString(31074)

destpath=xbmc.translatePath(os.path.join('special://home/addons/packages',''))

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1, localtxt3):
      shutil.rmtree(destpath)
      os.mkdir(destpath)
      self.close()

      xbmc.executebuiltin("Notification("+localtxt2+",XBMCHub TEAM)")


mydisplay = MyClass()
del mydisplay

