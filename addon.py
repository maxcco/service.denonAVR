import os
import xbmc
import xbmcaddon

__addon__ = xbmcaddon.Addon()
__cwd__ = __addon__.getAddonInfo('path')
__profile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib'))

sys.path.append(__resource__)

import utils
from service import DenonController

utils.log("Service starting...")
CONTROLLER = DenonController()
CONTROLLER.runProgram()
