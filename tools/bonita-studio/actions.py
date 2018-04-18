#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt/Bonita-Studio"]
IgnoreAutodep = True
WorkDir = "."
Version =  get.srcVERSION()

def setup():
    shelltools.system("unzip BonitaStudioCommunity-%s.zip" % Version)
    shelltools.system("mkdir BonitaStudioCommunity-%s/workspace" % Version)
    shelltools.system("chmod -R 777 BonitaStudioCommunity-%s/workspace" % Version)

def install():
    pisitools.insinto("/opt/BonitaStudio", "BonitaStudioCommunity-%s/*" % Version)
    pisitools.dosym("/opt/BonitaStudio/BonitaStudioCommunity64-linux", "/usr/bin/bonita-studio")
    
