# script by Mikey1234

import xbmc, xbmcgui
import shutil

localtxt1 = xbmc.getLocalizedString(31063)
localtxt2 = xbmc.getLocalizedString(31073)
localtxt4 = xbmc.getLocalizedString(31077)
localtxt5 = xbmc.getLocalizedString(31078)
localtxt6 = xbmc.getLocalizedString(31079)

path = os.path.join(xbmc.translatePath('special://home'),'userdata', 'sources.xml')

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1, localtxt4):
      if not os.path.exists(path):
          f = open(path, mode='w')
          f.write('<sources><files><source><name>FUSION</name><path pathversion="1">http://fusion.xbmchub.com</path></source></files></sources>')
          f.close()
          dialog = xbmcgui.Dialog()
          dialog.ok("XBMCHub TEAM","", localtxt5)
          return
        
      f   = open(path, mode='r')
      str = f.read()
      f.close()
      if 'http://fusion.xbmchub.com' in str:
          dialog = xbmcgui.Dialog()
          if dialog.yesno("XBMCHub TEAM","", localtxt6):
              xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
              xbmc.executebuiltin("XBMC.ActivateWindow(AddonBrowser)")
      if not'http://fusion.xbmchub.com' in str:
          if '</files>' in str:
              str = str.replace('</files>','<source><name>FUSION</name><path pathversion="1">http://fusion.xbmchub.com</path></source></files>')
              dialog = xbmcgui.Dialog()
              dialog.ok("XBMCHub TEAM","", localtxt5)
              f = open(path, mode='w')
              f.write(str)
              f.close()
          else:
              str = str.replace('</sources>','<files><source><name>FUSION</name><path pathversion="1">http://fusion.xbmchub.com</path></source></files></sources>')
              dialog = xbmcgui.Dialog()
              dialog.ok("XBMCHub TEAM","", localtxt5)
              f = open(path, mode='w')
              f.write(str)
              f.close()

mydisplay = MyClass()
del mydisplay


