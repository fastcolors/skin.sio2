# script by Mikey1234 & Fastcolors

import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os
import urllib2,urllib
import re

howto='http://dl.dropbox.com/u/129714017/XBMC%20HUB%20GUIDES/txts/howto.txt'
selected='special://skin/media/images/buttonselect.png'

#get actioncodes from https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h
ACTION_PREVIOUS_MENU = 10

class MyClass(xbmcgui.Window):
  def __init__(self):
    self.setCoordinateResolution(0)
    self.strActionInfo = xbmcgui.ControlLabel(960, 80, 960, 50, '', 'Size42B', '0xFFFFFFFF', alignment=2)
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('VideoHelp')
    self.list = xbmcgui.ControlList(1000, 161, 890, 900, 'Size33', '0xFFDDDDDD', '' ,'images/buttonselect.png', '0xFFFFFFFF',0,0,20,0,81)
    self.addControl(self.list)
    req = urllib2.Request(howto)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    fanart=""
    match=re.compile('i="(.+?)" n="(.+?)" u="(.+?)" d="(.+?)"').findall(link)
    for icon, name, youtube , description in match:
      if icon=='none':
          iconimage = 'http://i.ytimg.com/vi/%s/0.jpg' % youtube
      else:
          iconimage=str(icon)
      fanart=str(fanart)
      url = 'plugin://plugin.video.youtube/?path=root/video&action=play_video&videoid=%s' % youtube 
      url = str(url)
      listitem = xbmcgui.ListItem(name)
      listitem.setProperty('path' , url)
      self.list.addItem(listitem)
    self.setFocus(self.list)
    
  def onControl(self, control):
    if control == self.list:
      listitem = self.list.getSelectedItem()
      url=listitem.getProperty('path')
      print url
      xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(url)

  def message(self, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(" My message title", message)
 
mydisplay = MyClass()
mydisplay.doModal()
del mydisplay
