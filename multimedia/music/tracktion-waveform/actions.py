#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf Waveform-installer-64bit-linux-%s.deb" % Version)
    shelltools.system("tar xf data.tar.lzma")

def install():
    pisitools.insinto("/", "usr")
