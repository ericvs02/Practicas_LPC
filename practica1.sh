#!/bin/bash
 #Solicitando estado del tiempo general:
curl -s "https://api.openweathermap.org/data/2.5/onecall?lat=25.678613&lon=-100.455304&appid=85e207613dbc15db58435500833ab495">clima.txt
#Soliciando datos del clima al momento:
curl -s "https://api.openweathermap.org/data/2.5/onecall?lat=25.678613&lon=-100.455304&appid=85e207613dbc15db58435500833ab495" |       jq '.current'  > reporteactualclima.txt
#Solicitando la sensacion termica actual:
curl -s "https://api.openweathermap.org/data/2.5/onecall?lat=25.67813&lon=-100.455304&appid=85e207613dbc15db58435500833ab495" |      jq '.current.feels_like' > sensaciontermica.txt 
#FIN
