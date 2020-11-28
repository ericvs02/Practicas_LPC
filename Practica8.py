from ftplib import FTP, FTP_PORT
import os

ftp = FTP('ftp.us.debian.org') 
ftp.login()

#ftp.retrbinary('RETR', open(destination +'README', 'wb').write)
path = r"C:\Users\ERICV\Desktop\TXT"#Creamos la carpeta para copiar los archvios
os.mkdir(path)
filelist=ftp.nlst()
for file in filelist:
    if file.endswith('.msg')==True:
        print(file)
        ftp.retrbinary('RETR ' + file, open(path, 'wb').write)
    #ftp.retrbinary('RETR', open(file, 'wb').write)

    try:
        ftp.cwd(file)#checa si es una carpeta
        ftp.pwd()
        files=ftp.nlst()#Lista los archivos de la carpeta
        for f in files:
            print (f)
            if f.startswith("README") == True:
                ftp.retrbinary('RETR ' + f, open(path, 'wb').write)    
            
        
    except:
        print("Archivo: ",file ,"No es una carpeta")
  
ftp.quit()
