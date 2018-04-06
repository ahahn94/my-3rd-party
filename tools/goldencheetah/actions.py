#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools
import shutil


NoStrip = ["/"]
IgnoreAutodep = True
Version =  get.srcVERSION()

def setup():
    shelltools.system("ar xf GoldenCheetah_V%s*amd64.deb" % Version)
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "etc")
    pisitools.dosym("/opt/GoldenCheetah/GoldenCheetah", "/usr/bin/GoldenCheetah")
