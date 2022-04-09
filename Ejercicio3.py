import serial
import time
from matplotlib import image
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image


arduino = serial.Serial('COM3', 9600, timeout=1)
print('Conectado')


hot = 30
cold = 26

def imge():
    ventana = Tk()
    ventana.title('Panic!')
    ventana.iconbitmap(r'D:\5TO_SEMESTRE\PROGRA_III\Laboratorio8\ppp.ico')

    imagen = ImageTk.PhotoImage(Image.open(r'D:\5TO_SEMESTRE\PROGRA_III\Laboratorio8\temp.jpg').resize((500,500)))
    boton = Button(image=imagen, command=ventana.quit)
    boton.pack()
    ventana.mainloop()

while True:
    data = arduino.readline().decode().strip()
    time.sleep(1)

    if data:
        data = float(data)
        print(data)

        if data >= hot:
            print(imge())