import xbmc
import xbmcaddon
import requests

ADDON_ID = 'service.denonavr'
ADDON = xbmcaddon.Addon(ADDON_ID)
CWD = ADDON.getAddonInfo('path').decode('utf-8')

def log(message, loglevel=xbmc.LOGNOTICE):
    xbmc.log(encode(ADDON_ID+ "-" + ADDON.getAddonInfo('version') + " : " + message), level=loglevel)

def encode(string):
    return string.encode('UTF-8', 'replace')

def post(data, count_err=0):
    ipDenon = ADDON.getSetting('ipDenon')
    if count_err < 10:
        try:
            requests.post("http://"+ ipDenon +"/MainZone/index.put.asp", data, verify=False, timeout=2)
        except Exception:
            # try again
            count_err += 1
            return post(data, count_err)
    else:
        log("Can not reach the denonavr at ip : "+ ipDenon +", please check your settings", xbmc.LOGERROR)
