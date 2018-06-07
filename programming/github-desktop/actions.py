#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools
import shutil

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("ar xf GitHubDesktop-linux-amd64-%s.deb" % Version)
    shelltools.system("tar xf data.tar.xz")

def install():
    shutil.rmtree("usr/share/applications")
    shutil.rmtree("usr/share/icons")
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")