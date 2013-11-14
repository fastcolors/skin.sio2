# script by Fastcolors

import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os
import xml.dom.minidom as minidom
import sys
import md5

set = "lockmode"
prnum= sys.argv[ 1 ]

#----------------------------------------------------------------------
def getSetting(xml):
    doc = minidom.parse(xml)
    node = doc.documentElement
    profiles = doc.getElementsByTagName("profile")
 
    settings = []
    checks= []
    codes=[]
    for profile in profiles:
        checkObj = profile.getElementsByTagName("name")[0]
        checks.append(checkObj)
        
    for check in checks:
        nodes = check.childNodes
        for node in nodes:
          print '____________________USER____________________________'
          cazz = node.data
          print cazz
          if cazz in prnum:
             for profile in profiles:
              contObj = profile.getElementsByTagName(set)[0]
              settings.append(contObj)
              codeObj = profile.getElementsByTagName('lockcode')[0]
              codes.append(codeObj)
    
    for code in codes:
      nodes = code.childNodes
      for node in nodes:
        code = node.data
        print '_____________________PASSWORD___________________________'
        print code
      
    for setting in settings:
        nodes = setting.childNodes
        for node in nodes:
            print '_________________PASSWORD FLAG_______________________________'
            print node.data
            ricazz = node.data
            ricazz = int(ricazz)
            
            if ricazz == 0:
              print ricazz
              xbmc.executebuiltin('ActivateWindow(' + sys.argv[ 2 ] + ')')
              quit()
            kb = xbmc.Keyboard()
            kb.setHeading('Enter password') # optional
            kb.setHiddenInput(True) # optional
            kb.doModal()
            if (kb.isConfirmed()):
              choice = kb.getText()
              m = md5.new(choice).hexdigest()
              print '_____________________INPUT MD5___________________________'
              
              print m
              
              if m in code:
                xbmc.executebuiltin('ActivateWindow(' + sys.argv[ 2 ] + ')')


if __name__ == "__main__":
    document = xbmc.translatePath(os.path.join('special://home/userdata/','profiles.xml'))
    getSetting(document)