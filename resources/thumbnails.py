
import xbmc, xbmcgui
import shutil

localtxt1 = xbmc.getLocalizedString(31066)
localtxt2 = xbmc.getLocalizedString(31073)
localtxt3 = xbmc.getLocalizedString(31074)

thumbnails=xbmc.translatePath(os.path.join('special://home/userdata/Thumbnails',''))
thumbdatabase=xbmc.translatePath(os.path.join('special://home/userdata/Database',''))

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1, localtxt3):
      shutil.rmtree(thumbnails)
      os.mkdir(thumbnails)
      import glob
      for db in glob.glob(os.path.join(thumbdatabase, 'Textures*.*')):
        from sqlite3 import dbapi2 as sqlite3
        try:
          db   = xbmc.translatePath(db)
          conn = sqlite3.connect(db, timeout = 10, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)
          c    = conn.cursor()

          c.execute("DELETE FROM texture WHERE id > 0")       
          c.execute("VACUUM")       

          conn.commit()
          c.close()
        except:
          pass
      self.close()

      xbmc.executebuiltin("Notification("+localtxt2+",XBMCHub TEAM)")


mydisplay = MyClass()
del mydisplay

