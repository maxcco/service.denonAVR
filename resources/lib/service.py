import sys
import xbmc
import xbmcgui
import xbmcaddon
import utils


class PlayerMonitor(xbmc.Player):

    def __init__(self):
        xbmc.Player.__init__(self)
        utils.post({'cmd0':'PutSurroundMode/MOVIE', 'cmd1':'aspMainZone_WebUpdateStatus/'})
        self.currentMode = "MOVIE"

    def onPlayBackStarted(self):
        if (self.isPlayingAudio() and self.currentMode != "MUSIC"):
            utils.log('Changing to Music Mode', xbmc.LOGINFO)
            utils.post({'cmd0':'PutSurroundMode/MUSIC', 'cmd1':'aspMainZone_WebUpdateStatus/'})
            self.currentMode = "MUSIC"

        if (self.isPlayingVideo() and self.currentMode != "MOVIE"):
            utils.log('Changing to Music Mode', xbmc.LOGINFO)
            utils.post({'cmd0':'PutSurroundMode/MOVIE', 'cmd1':'aspMainZone_WebUpdateStatus/'})
            self.currentMode = "MOVIE"


class DenonController():
    player_monitor = None

    def __init__(self):
        self.player_monitor = PlayerMonitor()


    def runProgram(self):
        while not xbmc.abortRequested:
            # waiting loop
            xbmc.sleep(500)

        #clean up monitor on exit
        del self.player_monitor
