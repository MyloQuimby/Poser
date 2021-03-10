import poser
import wx
import wx.py
import wx.aui
import poseraddon

class PythonShell(poseraddon.Addon):
    def __init__(self):
        self.addonInfo['id'] = 'com.smithmicro.pythonShell'
        self.addonInfo['author'] = 'Smith Micro, Inc'
        self.addonInfo['copyright'] = '(c) 2012 Smith Micro, Inc'
        self.addonInfo['name'] = 'Python Shell'
        self.addonInfo['version'] = '1.0'
        self.addonInfo['observer'] = 0
        self.addonInfo['scenedata'] = 0
    
    def load(self):        
    	man = poser.WxAuiManager()
        root = man.GetManagedWindow()
        win = wx.py.shell.Shell(root, introText="Welcome to the Poser Python shell.")
        man.AddPane(win, wx.aui.AuiPaneInfo().DefaultPane().Name("com.smithmicro.pythonShell").Caption("Python Shell").Hide().FloatingSize(wx.Size(450, 300)))
       
    def unload(self):
        pass
         
poser.RegisterAddon("com.smithmicro.pythonShell", PythonShell())
