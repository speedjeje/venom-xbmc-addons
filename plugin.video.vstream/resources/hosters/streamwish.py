# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
#

from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.hosters.hoster import iHoster

class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'streamwish', 'StreamWish')

    def _getMediaLinkForGuest(self):
        api_call = ''

        oParser = cParser()
        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        sPattern = '{file:"([^"]+)"'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0] is True:
            api_call = aResult[1][0]

        if api_call:
            return True, api_call

        return False, False