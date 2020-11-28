#!/bin/bash
echo "IP local : " > practica7.txt
hostname -I >> practica7.txt 

echo "IP publica :" >> practica7.txt
curl ifconfig.me >> practica7.txt

echo "nmap al segmento de red:" >> practica7.txt
nmap 192.168.100.1-24 >> practica7.txt
 

echo "nmap a scanme.nmap.org con hostmap-bfk.nse:" >> practica7.txt
nmap  --script hostmap-bfk.nse scanme.nmap.org >> practica7.txt

echo "nmap a nuestra ip publica:" >> practica7.txt
ipPublica=$(curl ifconfig.me)
nmap $ipPublica >> practica7.txt

base64 < practica7.txt > practica7_encoded


