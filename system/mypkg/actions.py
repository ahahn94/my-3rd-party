#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools
import shutil


NoStrip = ["/"]
IgnoreAutodep = True
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")