
import serial


ard = serial.Serial('COM3', 9600)

while 1:
  datos = ard.readline()
  #temp = datos[10:20]
  #humedad = datos[38:70]
  #print("La temperatura es: ",temp, "La humedad es: ", humedad)
  print(datos)   
           
               

        











