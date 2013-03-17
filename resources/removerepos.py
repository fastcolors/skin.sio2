#includes scripts by Mikey1234 - Spoyser.

from sqlite3 import dbapi2 as sqlite3
import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os
import urllib2,urllib
import re
import shutil
import glob

howto='http://dl.dropbox.com/u/129714017/XBMC%20HUB%20GUIDES/txts/howto.txt'
dialog = xbmcgui.Dialog()
pluginpath = xbmc.translatePath(os.path.join('special://home/addons',''))
localtxt1 = xbmc.getLocalizedString(31081)

class MyClass(xbmcgui.Window):
  def __init__(self):
    self.setCoordinateResolution(0)
    self.list = xbmcgui.ControlList(500, 161, 1420, 900, 'Size36', '0xFFDDDDDD', '' ,'images/contextbutton.png', '',60,60,10,0,81,0)
    self.addControl(self.list)
    for file in glob.glob(os.path.join(pluginpath, 'repository.*')):
      name=str(file).replace(pluginpath,'')
      iconimage=(os.path.join(file,'icon.png'))
      listitem = xbmcgui.ListItem(name,'','',iconimage)
      self.list.addItem(listitem)
    self.setFocus(self.list)
    self.strActionInfo = xbmcgui.ControlLabel(0, 80, 1920, 50, '', 'Size42B', '0xFFFFFFFF', alignment=2)
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel(localtxt1)
    
  def onControl(self, control):
    if control == self.list:
      listitem = self.list.getSelectedItem().getLabel()
      plugin = xbmc.translatePath(os.path.join('special://home/addons',listitem))
      if dialog.yesno("Remove", '', "Do you want to Remove"):  
        DeleteAddon(listitem)
        print '__________________________NONREPO DELETE____________________________'
        self.list.reset() 
        for file in glob.glob(os.path.join(pluginpath, 'repository.*')):
          name=str(file).replace(pluginpath,'')
          iconimage=(os.path.join(file,'icon.png'))
          listitem = xbmcgui.ListItem(name,'','',iconimage)
          self.list.addItem(listitem)
      self.setFocus(self.list)

def RemoveAddon(dbPath, name):
    db   = xbmc.translatePath(dbPath)
    conn = sqlite3.connect(db, timeout = 10, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT id FROM addon WHERE addonID = ?", (name,)) 

    ids = []

    for row in c:
        ids.append(row["id"])

    for id in ids:       
        c.execute("DELETE FROM addon         WHERE id = ?",      (id,))
        c.execute("DELETE FROM addonextra    WHERE id = ?",      (id,))
        c.execute("DELETE FROM dependencies  WHERE id = ?",      (id,))
        c.execute("DELETE FROM addonlinkrepo WHERE idAddon = ?", (id,))

    c.execute("DELETE FROM disabled  WHERE addonID = ?", (name,))
    c.execute("DELETE FROM broken    WHERE addonID = ?", (name,))
    c.execute("DELETE FROM blacklist WHERE addonID = ?", (name,))

    c.execute("VACUUM")
    conn.commit()
    c.close()


def DeleteAddon(name):
    try:
        addon = xbmcaddon.Addon(id = name)
        print '___________________________' 
        print name
        print '___________________________' 
        path  = xbmc.translatePath(addon.getAddonInfo('path'))   
        shutil.rmtree(path)
        addondatafolder = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' , name))
        print '___________________________'
        print addondatafolder
        print '___________________________'
        shutil.rmtree(addondatafolder)
    except:
        print 'ERROR IN DELETING SOMETHING'

    dbPath = xbmc.translatePath('special://home/userdata/Database')
    files  = glob.glob(os.path.join(dbPath, 'Addons*.db'))
    for f in files:        
        try:
            RemoveAddon(f, name)
        except:
            pass

        
mydisplay = MyClass()
mydisplay.doModal()
del mydisplay
