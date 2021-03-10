import os, sys
#import Numeric
import poser

def _loadAddons(runtimeRoot):
    # Load addons to Poser
    try:
        addonpath = os.path.join(runtimeRoot, "Runtime", "Python", "addons")
        sys.path.append(addonpath)
        for addon in os.listdir(addonpath):
            fullpath = os.path.join(addonpath, addon)
            if(not(addon.startswith(".")) and os.path.isdir(fullpath)):    
                try:
                    __import__(addon)
                except Exception, err:
                    print "An errror occurred importing addon", addon, ":"
                    print 'ERROR: %s\n' % str(err)
    except:
        pass

#-------------------------------------------
# Load the default python button commands...
#   (use poser.ExecFile instead of execfile so we can use cross platform name, etc)
#-------------------------------------------

runtimeRoot = os.path.split(poser.AppLocation())[0]
mainButtonsPath = os.path.join(runtimeRoot, "Runtime", "Python", "PoserScripts", "mainButtons.py")
poser.ExecFile(mainButtonsPath)

_loadAddons(runtimeRoot)
for runtimePath in poser.Libraries():
    _loadAddons(runtimePath)
