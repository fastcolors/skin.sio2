# script by Mikey1234

import xbmc, xbmcgui,os
import shutil

localtxt1 = xbmc.getLocalizedString(31065)
localtxt2 = xbmc.getLocalizedString(31073)
localtxt3 = xbmc.getLocalizedString(31074)
localtxt4 = xbmc.getLocalizedString(31075)


class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1, localtxt4 ,"",localtxt3):
      xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
      if os.path.exists(xbmc_cache_path)==True:   
              for root, dirs, files in os.walk(xbmc_cache_path):
                      file_count = 0
                      file_count += len(files)
              
              # Count files and give option to delete
                      if file_count > 0:
      
                              dialog = xbmcgui.Dialog()
                              if dialog.yesno("Delete XBMC Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                              
                                      for f in files:
                                              os.unlink(os.path.join(root, f))
                                      for d in dirs:
                                              shutil.rmtree(os.path.join(root, d))
                                              
                      else:
                              pass
      if xbmc.getCondVisibility('system.platform.ATV2'):
              atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
              
              for root, dirs, files in os.walk(atv2_cache_a):
                      file_count = 0
                      file_count += len(files)
              
                      if file_count > 0:

                              dialog = xbmcgui.Dialog()
                              if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):
                              
                                      for f in files:
                                              os.unlink(os.path.join(root, f))
                                      for d in dirs:
                                              shutil.rmtree(os.path.join(root, d))
                                              
                      else:
                              pass
              atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
              
              for root, dirs, files in os.walk(atv2_cache_b):
                      file_count = 0
                      file_count += len(files)
              
                      if file_count > 0:

                              dialog = xbmcgui.Dialog()
                              if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):
                              
                                      for f in files:
                                              os.unlink(os.path.join(root, f))
                                      for d in dirs:
                                              shutil.rmtree(os.path.join(root, d))
                                              
                      else:
                              pass
                            # Set path to Cydia Archives cache files
              archive_cache_path =os.path.join('/private/var/cache/apt', 'archives')
              try:    
                      for root, dirs, files in os.walk(archive_cache_path):
                              file_count = 0
                              file_count += len(files)
                              
                      # Count files and give option to delete
                              if file_count > 0:
              
                                      dialog = xbmcgui.Dialog()
                                      if dialog.yesno("Delete 'Cydia Archived' Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                                      
                                              for f in files:
                                                      os.unlink(os.path.join(root, f))
              except: 
                      dialog = xbmcgui.Dialog()
                      dialog.ok("XBMCHUB TEAM", "Cant Delete Please SSH Into ATV2 And Run", "apt-get autoclean   Brought To You By XBMCHUB.COM")
                                                            

      # Set path to What th Furk cache files
      wtf_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.whatthefurk/cache'), '')
      if os.path.exists(wtf_cache_path)==True:    
              for root, dirs, files in os.walk(wtf_cache_path):
                      file_count = 0
                      file_count += len(files)
              
              # Count files and give option to delete
                      if file_count > 0:
      
                              dialog = xbmcgui.Dialog()
                              if dialog.yesno("Delete WTF Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                              
                                      for f in files:
                                              os.unlink(os.path.join(root, f))
                                      for d in dirs:
                                              shutil.rmtree(os.path.join(root, d))
                                              
                      else:
                              pass
                              
                              # Set path to 4oD cache files
      channel4_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.4od/cache'), '')
      if os.path.exists(channel4_cache_path)==True:    
              for root, dirs, files in os.walk(channel4_cache_path):
                      file_count = 0
                      file_count += len(files)
              
              # Count files and give option to delete
                      if file_count > 0:
      
                              dialog = xbmcgui.Dialog()
                              if dialog.yesno("Delete 4oD Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                              
                                      for f in files:
                                              os.unlink(os.path.join(root, f))
                                      for d in dirs:
                                              shutil.rmtree(os.path.join(root, d))
                                              
                      else:
                              pass
                              
                              # Set path to BBC iPlayer cache files
      iplayer_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache'), '')
      if os.path.exists(iplayer_cache_path)==True:    
              for root, dirs, files in os.walk(iplayer_cache_path):
                      file_count = 0
                      file_count += len(files)
              
              # Count files and give option to delete
                      if file_count > 0:
      
                              dialog = xbmcgui.Dialog()
                              if dialog.yesno("Delete BBC iPlayer Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                              
                                      for f in files:
                                              os.unlink(os.path.join(root, f))
                                      for d in dirs:
                                              shutil.rmtree(os.path.join(root, d))
                                              
                      else:
                              pass
                              
                              
                              # Set path to Simple Downloader cache files
      downloader_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/script.module.simple.downloader'), '')
      if os.path.exists(downloader_cache_path)==True:    
              for root, dirs, files in os.walk(downloader_cache_path):
                      file_count = 0
                      file_count += len(files)
              
              # Count files and give option to delete
                      if file_count > 0:
      
                              dialog = xbmcgui.Dialog()
                              if dialog.yesno("Delete Simple Downloader Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                              
                                      for f in files:
                                              os.unlink(os.path.join(root, f))
                                      for d in dirs:
                                              shutil.rmtree(os.path.join(root, d))
                                              
                      else:
                              pass
                              
                              # Set path to ITV cache files
      itv_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.itv/Images'), '')
      if os.path.exists(itv_cache_path)==True:    
              for root, dirs, files in os.walk(itv_cache_path):
                      file_count = 0
                      file_count += len(files)
              
              # Count files and give option to delete
                      if file_count > 0:
      
                              dialog = xbmcgui.Dialog()
                              if dialog.yesno("Delete ITV Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                              
                                      for f in files:
                                              os.unlink(os.path.join(root, f))
                                      for d in dirs:
                                              shutil.rmtree(os.path.join(root, d))
                                              
                      else:
                              pass
      
      xbmc.executebuiltin("Notification("+localtxt2+",XBMCHub TEAM)")


mydisplay = MyClass()
del mydisplay
