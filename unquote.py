# -*- coding: latin-1 -*-
import urllib.parse
from urllib.parse import ParseResult
try:
    import xbmc, xbmcvfs, xbmcgui, xbmcaddon
except:
    pass

def patch_unquote():
    urllib.unquote = unquote
    urllib2.unquote = unquote
    urlparse.unquote = unquote
    urllib.unquote_plus = unquote_plus
    urllib.quote_plus = quote_plus
    urllib.quote = quote
import sys, os
import urllib
import urllib.request
