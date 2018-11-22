#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf TracktionInstall_7_Linux_64Bit_latest.deb")
    shelltools.system("tar xf data.tar.lzma")

def install():
    pisitools.insinto("/", "usr")
