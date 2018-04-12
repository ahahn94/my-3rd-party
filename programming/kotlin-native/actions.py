#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools
import shutil

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("tar xzvf kotlin-native-linux-%s.tar.gz" % Version)

def install():
    shutil.rmtree("kotlin-native-linux-%s/samples" % Version)
    pisitools.insinto("/opt/kotlin-native", "kotlin-native-linux-%s/*" % Version)
    pisitools.dosym("/opt/kotlin-native/bin/cinterop", "/usr/bin/cinterop")
    pisitools.dosym("/opt/kotlin-native/bin/jsinterop", "/usr/bin/jsinterop")
    pisitools.dosym("/opt/kotlin-native/bin/klib", "/usr/bin/klib")
    pisitools.dosym("/opt/kotlin-native/bin/konanc", "/usr/bin/konanc")
    pisitools.dosym("/opt/kotlin-native/bin/kotlinc-native", "/usr/bin/kotlinc-native")
    pisitools.dosym("/opt/kotlin-native/bin/run_konan", "/usr/bin/run_konan")
