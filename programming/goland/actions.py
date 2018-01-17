#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    shutil.rmtree("GoLand-2017.3/jre64")
    pisitools.insinto("/opt/goland", "GoLand-*/*")
    pisitools.dosym("/opt/goland/bin/goland.sh", "/usr/bin/goland")
