#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("tar xzvf spring-tool-suite-%s*.tar.gz" % Version)

def install():
    pisitools.insinto("/usr/share/spring-tool-suite", "sts-bundle/*")
    pisitools.dosym("/usr/share/spring-tool-suite/sts-%s.RELEASE/STS" % Version, "/usr/bin/STS")
