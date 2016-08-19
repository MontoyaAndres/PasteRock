#-*- coding: utf-8 -*-
#Autor: Andrés Montoya (SpyRock)
#No me hago responsable del mal uso que este se le pueda dar.
#!/usr/bin/python
import sys
import os
from colores import *
class install(bcolors):
	def __init__(self):
		print bcolors.OKBLUE+"""
 ██▓███   ▄▄▄        ██████ ▄▄▄█████▓▓█████  ██▀███   ▒█████   ▄████▄   ██ ▄█▀   
▓██░  ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▒██▀ ▀█   ██▄█▒    
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▒██░  ██▒▒▓█    ▄ ▓███▄░    
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄    
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄   
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒   
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░   
░░         ░   ▒   ░  ░  ░    ░         ░     ░░   ░ ░ ░ ░ ▒  ░        ░ ░░ ░    
               ░  ░      ░              ░  ░   ░         ░ ░  ░ ░      ░  ░      
                                                              ░                  
"""
	def installrequerimientos(self):
		if not os.geteuid() == 0:
			sys.exit("""\033[1;91m\n[!] La instalación de PasteRock necesita permisos de root. ¯\_(ツ)_/¯\n\033[1;m""")
		else:
			os.system("cd .. && cd.. && mv PasteRock /opt/")
			os.system("cp pasterock /usr/bin && chmod +x /usr/bin/pasterock")
			
			print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Comprobando si Metasploit Framework esta instalado...!\n"
			if os.path.exists("/opt/metasploit-framework"):
				print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"True...!\n"
			else:
				print bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"False...!\n"
				MetasploitNoInstalled = raw_input(bcolors.payload+("¿Quiere instalar metasploit? (y/n) "))
				if MetasploitNoInstalled == "y":
					print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Instalando Metasploit Framework...!\n"
					os.system("chmod +x metasploit && ./metasploit")
				else:
					pass
			print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Comprobando si Apache2 esta instalado...!\n"
			if os.path.exists("/var/www/html/"):
				print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"True...!"
			else:
				print bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Fail...!\n"
				apache = raw_input(bcolors.payload+"¿Quiere instalar Apache2? (y/n) ")
				if apache == "y":
					print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Instalando Apache2...!"
					os.system("apt-get install apache2")
				else:
					pass
		print bcolors.WARNING+"\nInstalación finalizada."
Iniciar = install()
Iniciar.installrequerimientos()
