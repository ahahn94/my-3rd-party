#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/dotnet-core", "dotnet")
    pisitools.insinto("/opt/dotnet-core", "host")
    pisitools.insinto("/opt/dotnet-core", "sdk")
    pisitools.insinto("/opt/dotnet-core", "shared")
    pisitools.insinto("/opt/dotnet-core", "LICENSE.txt")
    pisitools.insinto("/opt/dotnet-core", "ThirdPartyNotices.txt")
    pisitools.dosym("/opt/dotnet-core/dotnet", "/usr/bin/dotnet")
