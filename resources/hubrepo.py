# script by Mikey1234

import xbmc, xbmcgui
import shutil
import urllib2,urllib

localtxt1 = xbmc.getLocalizedString(31072)
localtxt2 = xbmc.getLocalizedString(31073)

def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("XBMCHUB...Maintenance","Downloading & Copying File",'')
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print 'Downloaded '+str(percent)+'%'
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("", localtxt1):
        url = 'http://xbmc-hub-repo.googlecode.com/svn/addons/repository.xbmchub/repository.xbmchub-1.0.1.zip'
        path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
        lib=os.path.join(path, 'repository.xbmchub-1.0.1.zip')
        DownloaderClass(url,lib)
        addonfolder = xbmc.translatePath(os.path.join('special://home/addons',''))
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,addonfolder))


       xbmc.executebuiltin("Notification("+localtxt2+",XBMCHub TEAM)")
      mydisplay = MyClass()
del mydisplay