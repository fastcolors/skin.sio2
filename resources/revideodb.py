import xbmc, xbmcgui
import shutil
import glob, os

localtxt1 = xbmc.getLocalizedString(31084)
localtxt2 = xbmc.getLocalizedString(31073)
localtxt3 = xbmc.getLocalizedString(31074)
dialog = xbmcgui.Dialog()
path = xbmc.translatePath(os.path.join('special://home/userdata/Database',''))

class MyClass(xbmcgui.Window):
  def __init__(self):
    if dialog.yesno(localtxt1, localtxt3):
      database = os.path.join(path, 'MyVideos*.db')
      print database
      filelist = glob.glob(database)
      print filelist
      if filelist != []:
        for f in filelist:
          print f
          os.remove(f)
          xbmc.executebuiltin("Notification("+localtxt2+",XBMCHub TEAM)")
      else:
        print 'merdaa'
        xbmc.executebuiltin("Notification(File doesn't exists,XBMCHub TEAM)")

mydisplay = MyClass()
del mydisplay